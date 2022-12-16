import logging
import time

from ocs_ci.ocs.ui.base_ui import PageNavigator
from ocs_ci.ocs.ui.helpers_ui import get_blockpool_ui_element
from ocs_ci.ocs.ui.views import locators
from ocs_ci.utility.utils import get_ocp_version
from selenium.webdriver.common.by import By
from ocs_ci.helpers.helpers import create_unique_resource_name
from ocs_ci.ocs.exceptions import PoolStateIsUnknow
import ocs_ci.ocs.resources.pod as pod
from ocs_ci.utility import version

logger = logging.getLogger(__name__)


class BlockPoolUI(PageNavigator):
    """
    User Interface Selenium for Block Pools page

    """

    def __init__(self, driver):
        super().__init__(driver)
        ocp_version = get_ocp_version()
        self.bp_loc = locators[ocp_version]["block_pool"]
        self.sc_loc = locators[ocp_version]["storageclass"]

    def create_pool(self, replica, compression):
        """
        Create block pool via UI

        Args:
            replica (int): replica size usually 2,3
            compression (bool): True to enable compression otherwise False

        Return:
            array: pool name (str) pool status (bool) #pool can be created with failure status

        """
        pool_name = create_unique_resource_name("test", "rbd-pool")
        self.navigate_block_pool_page()
        self.do_click(self.bp_loc["create_block_pool"])
        self.do_send_keys(self.bp_loc["new_pool_name"], pool_name)
        self.do_click(self.bp_loc["first_select_replica"])
        if replica == 2:
            self.do_click(self.bp_loc["second_select_replica_2"])
        else:
            self.do_click(self.bp_loc["second_select_replica_3"])
        if compression is True:
            self.do_click(self.bp_loc["conpression_checkbox"])
        self.do_click(self.bp_loc["pool_confirm_create"])
        wait_for_text_result = self.wait_until_expected_text_is_found(
            self.bp_loc["pool_state_inside_pool"], "Ready", timeout=15
        )
        if wait_for_text_result is True:
            logger.info(f"Pool {pool_name} was created and it is in Ready state")
            return [pool_name, True]
        else:
            logger.info(f"Pool {pool_name} was created but did not reach Ready state")
            return [pool_name, False]

    def check_pool_existence(self, pool_name):
        """
        Check if pool appears in the block pool list

        Args:
            pool_name (str): Name of the pool to check

        Return:
            bool: True if pool is in the list of pools page, otherwise False

        """
        self.navigate_overview_page()
        self.navigate_block_pool_page()
        self.page_has_loaded(retries=10)
        if self.ocp_version_full >= version.VERSION_4_9:
            pool_existence = self.wait_until_expected_text_is_found(
                (f"a[data-test={pool_name}]", By.CSS_SELECTOR), pool_name, 5
            )
        else:
            pool_existence = self.wait_until_expected_text_is_found(
                (f"a[data-test-operand-link={pool_name}]", By.CSS_SELECTOR),
                pool_name,
                5,
            )
        logger.info(f"Pool name {pool_name} existence is {pool_existence}")
        return pool_existence

    def delete_pool(self, pool_name):
        """
        Delete pool from pool page

        Args:
            pool_name (str): The name of the pool to be deleted

        Returns:
            bool: True if pool is not found in pool list, otherwise false

        """

        logger.info(f"Deleting the blockpool: {pool_name}")
        self.select_blockpool(pool_name)
        self.do_click(self.bp_loc["actions_inside_pool"])
        self.do_click(self.bp_loc["delete_pool_inside_pool"])
        self.do_click(self.bp_loc["confirm_delete_inside_pool"])
        # wait for pool to deleted
        time.sleep(2)
        logger.info(f"Checking if {pool_name} exists in the Block Pools UI list.")
        return not self.check_pool_existence(pool_name)

    def edit_pool_parameters(self, pool_name, replica=3, compression=True):
        """
        Edit an already existing pool

        Args:
            pool_name (str): The name of the pool to change.
            replica (int): size of replica. Available in OCS now 2,3.
            compression (bool): True if enable compression. False otherwise.

        """
        self.navigate_overview_page()
        self.navigate_block_pool_page()
        self.page_has_loaded()
        self.do_click([f"{pool_name}", By.LINK_TEXT])
        self.do_click(self.bp_loc["actions_inside_pool"])
        self.do_click(self.bp_loc["edit_pool_inside_pool"])
        self.do_click(self.bp_loc["replica_dropdown_edit"])
        if replica == 2:
            self.do_click(self.bp_loc["second_select_replica_2"])
        else:
            self.do_click(self.bp_loc["second_select_replica_3"])
        compression_checkbox_status = self.get_checkbox_status(
            self.bp_loc["compression_checkbox_edit"]
        )
        if compression != compression_checkbox_status:
            self.do_click(self.bp_loc["compression_checkbox_edit"])
        self.do_click(self.bp_loc["save_pool_edit"])

    def reach_pool_limit(self, replica, compression):
        """
        Add pools till pool fails because of pg limit.

        Args:
             replica (int): size of pool.
             compression (bool): True for enabling compression. Otherwise False.

        """
        pool_list = []
        ceph_pod = pod.get_ceph_tools_pod()
        count = 0
        while count < 50:
            count += 1
            pool_name, pool_status = self.create_pool(replica, compression)
            pool_list.append(pool_name)
            if pool_status is True:
                ceph_status = ceph_pod.exec_ceph_cmd(ceph_cmd="ceph status")
                total_pg_count = ceph_status["pgmap"]["num_pgs"]
                logger.info(f"Total pg count is {total_pg_count}")
                continue
            else:
                wait_for_text_result = self.wait_until_expected_text_is_found(
                    self.bp_loc["pool_state_inside_pool"], "Failure", timeout=10
                )
                if wait_for_text_result is True:
                    logger.info(f"Pool {pool_name} is in failure state")
                    self.take_screenshot()
                    ceph_status = ceph_pod.exec_ceph_cmd(ceph_cmd="ceph status")
                    total_pg_count = ceph_status["pgmap"]["num_pgs"]
                    logger.info(f"Total pg count is {total_pg_count}")
                    for pool in pool_list:
                        self.delete_pool(pool)
                    break
                else:
                    pool_state = self.get_element_text(
                        self.bp_loc["pool_state_inside_pool"]
                    )
                    logger.info(f"pool condition is {pool_state}")
                    for pool in pool_list:
                        self.delete_pool(pool)
                    raise PoolStateIsUnknow(
                        f"pool {pool_name} is in unexpected state {pool_state}"
                    )

    def pool_raw_capacity_loaded(self, pool_name):
        """
        Takes pool name and returns True if the raw capacity of the block pool is loaded
        or returns False if the capacity is not loaded.

        Args:
            pool_name (str): The name of the pool to be deleted

        Returns:
            bool: True if raw capacity of the blockpool is loaded, otherwise False

        """
        logger.info("Checking if the Block Pool Raw Capacity has loaded in UI")

        self.select_blockpool(pool_name)

        raw_capacity_loaded = self.check_element_text(
            "Available",
            "div[@class='ceph-raw-card-legend__title']",
        )
        if raw_capacity_loaded:
            logger.info("Block Pool Raw Capacity has loaded in UI")
        else:
            logger.warning("Block Pool Raw Capacity has not loaded in UI")
        return raw_capacity_loaded

    def cross_check_raw_capacity(self, pool_name):
        """
        Takes pool name and returns True if the raw capacity of the block pool is same in GUI as obtained from CLI
        or returns False if the raw capacity of the block pool doesnt match with CLI

        Args:
            pool_name (str): The name of the pool to be deleted

        Returns:
            bool: True if raw capacity of the blockpool is is same in GUI as obtained from CLI, otherwise False

        """
        logger.info(
            "Checking if the Block Pool Raw Capacity is same in GUI as obtained from CLI"
        )
        if self.pool_raw_capacity_loaded(pool_name):
            cmd = "rados df"
            ct_pod = pod.get_ceph_tools_pod()
            df_op = ct_pod.exec_ceph_cmd(ceph_cmd=cmd)
            for pools in df_op["pools"]:
                if pools["name"] == pool_name:
                    raw_capacity = round(
                        int(pools["size_kb"]) / 1024, 1
                    )  # converting it into MiB because we are only running io in MiB in the previous step

            logger.info(
                f"Raw capacity of {pool_name} is {raw_capacity} MiB as checked by CLI"
            )

            used_raw_capacity_in_UI = self.get_element_text(
                self.bp_loc["used_raw_capacity_in_UI"]
            )

            if used_raw_capacity_in_UI == f"{str(raw_capacity)} MiB":
                logger.info("UI values did matched as per CLI for the Raw Capacity")
                return True
            else:
                logger.error(
                    f"UI value (i.e {used_raw_capacity_in_UI}) did not matched as per CLI for the Raw Capacity"
                )
                return False

    def select_blockpool(self, pool_name):
        """
        Selects and clicks on the blocpool according to the blockpool name passed.

        Args:
            pool_name (str): Block pool name that is to be selected.

        Returns:
            True (bool): Successfull selection of the blockpool

        """
        self.navigate_overview_page()
        self.navigate_block_pool_page()
        self.page_has_loaded()
        if self.ocp_version_full <= version.VERSION_4_8:
            self.do_click(get_blockpool_ui_element(pool_name, version.VERSION_4_8))
        else:
            self.do_click(get_blockpool_ui_element(pool_name, self.ocp_version_full))

        return True
