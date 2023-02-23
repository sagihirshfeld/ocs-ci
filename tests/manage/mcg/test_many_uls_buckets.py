import logging

import pytest

from ocs_ci.framework.testlib import (
    tier2,
    bugzilla,
    skipif_aws_creds_are_missing,
    skipif_disconnected_cluster,
    skipif_proxy_cluster,
    skipif_mcg_only,
)

from ocs_ci.ocs import constants

logger = logging.getLogger(__name__)


@tier2
@skipif_disconnected_cluster
@skipif_proxy_cluster
@bugzilla("2151903")
class TestManyUlSBuckets:
    """
    Test MCG functionality when there are many ULS buckets/blobs.
    """

    DEFAULT_REGION = "us-east-2"
    MANY_BUCKETS_NUM = 100

    @pytest.mark.parametrize(
        argnames="uls_provider",
        argvalues=[
            pytest.param(
                "rgw",
                marks=[skipif_mcg_only],
                id="RGW",
            ),
            pytest.param(
                "aws",
                marks=[skipif_aws_creds_are_missing],
                id="AWS",
            ),
            pytest.param(
                "gcp",
                id="GCP",
            ),
            pytest.param("azure", id="AZURE"),
            pytest.param(
                "ibmcos",
                id="IBMCOS",
            ),
        ],
    )
    def test_mcg_stores_creation_with_many_uls(
        self, backingstore_factory, namespacestore_factory, uls_provider, mcg_obj
    ):
        """
        Test new Backingstore/Namespacestore health when there are many buckets/blobs
        in the ULS provider.
        """

        logger.info(f"Creating {self.MANY_BUCKETS_NUM} {uls_provider} NamespaceStores")
        for i in 100:
            logger.info(f"Creating Namespacestore {i + 1} / {self.MANY_BUCKETS_NUM}")
            namespacestore = namespacestore_factory(
                "oc", {uls_provider: [(1, self.DEFAULT_REGION)]}
            )[0]
            assert (
                namespacestore.verify_health()
            ), f"Failed in creating the first {self.MANY_BUCKETS_NUM} NamespaceStores"

        logger.info("Creating additional MCG stores with the same ULS provider:")
        cli_nss = namespacestore_factory(
            "cli", {uls_provider: [(1, self.DEFAULT_REGION)]}
        )[0]
        assert cli_nss.verify_health()

        oc_nss = namespacestore_factory(
            "oc", {uls_provider: [(1, self.DEFAULT_REGION)]}
        )[0]
        assert oc_nss.verify_health()

        cli_bs = backingstore_factory(
            "cli", {uls_provider: [(1, self.DEFAULT_REGION)]}
        )[0]
        assert mcg_obj.check_backingstore_state(cli_bs.name, constants.BS_OPTIMAL)

        oc_bs = backingstore_factory("oc", {uls_provider: [(1, self.DEFAULT_REGION)]})[
            0
        ]

        assert mcg_obj.check_backingstore_state(oc_bs.name, constants.BS_OPTIMAL)
