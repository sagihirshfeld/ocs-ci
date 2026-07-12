import logging

import pytest

from ocs_ci.framework import config
from ocs_ci.framework.pytest_customization.marks import (
    mcg,
    red_squad,
    skipif_disconnected_cluster,
    skipif_external_mode,
    skipif_managed_service,
)
from ocs_ci.framework.testlib import MCGTest, tier2
from ocs_ci.ocs import constants
from ocs_ci.ocs.exceptions import CommandFailed, TimeoutExpiredError
from ocs_ci.ocs.ocp import OCP
from ocs_ci.ocs.resources.objectbucket import OBC
from ocs_ci.ocs.resources.pod import get_pods_having_label
from ocs_ci.ocs.warp import WarpWorkloadRunner
from ocs_ci.utility.utils import TimeoutSampler

logger = logging.getLogger(__name__)


@mcg
@red_squad
@skipif_disconnected_cluster
@skipif_external_mode
@skipif_managed_service
@tier2
class TestNooBaaEndpointKeda(MCGTest):
    """
    Test NooBaa endpoint autoscaling with KEDA.

    Setting spec.multiCloudGateway.autoscaler.autoscalerType=keda on
    the StorageCluster makes the ocs-operator propagate it to the
    NooBaa CR, which in turn makes the noobaa-operator create a
    ScaledObject with a CPU utilization trigger, replacing the
    default HPA.
    """

    MIN_ENDPOINT_COUNT = 1
    MAX_ENDPOINT_COUNT = 2

    @pytest.fixture(scope="class")
    def setup_keda_autoscaling(self, request, keda_class):
        """
        Configure KEDA-based autoscaling for NooBaa endpoints.

        1. Set endpoint min/max counts and autoscalerType=keda via StorageCluster
        2. Wait for the noobaa-operator to create a ScaledObject and delete the HPA
        3. Wait for endpoints to stabilize at minCount
        """
        namespace = config.ENV_DATA["cluster_namespace"]
        sc_ocp = OCP(kind=constants.STORAGECLUSTER, namespace=namespace)
        sc_resource = sc_ocp.get()["items"][0]
        sc_name = sc_resource["metadata"]["name"]

        # Save original values for restoration
        mcg_spec = sc_resource.get("spec", {}).get("multiCloudGateway", {})
        endpoints_spec = mcg_spec.get("endpoints", {})
        original_min = endpoints_spec.get("minCount", 1)
        original_max = endpoints_spec.get("maxCount", 2)
        original_autoscaler_type = mcg_spec.get("autoscaler", {}).get(
            "autoscalerType", "hpav2"
        )

        def finalizer():
            logger.info(
                f"Restoring endpoint counts to min={original_min}, "
                f"max={original_max} and autoscaler to {original_autoscaler_type}"
            )
            try:
                sc_ocp.patch(
                    resource_name=sc_name,
                    params=(
                        f'{{"spec":{{"multiCloudGateway":{{'
                        f'"endpoints":{{"minCount":{original_min},"maxCount":{original_max}}},'
                        f'"autoscaler":{{"autoscalerType":"{original_autoscaler_type}"}}'
                        f"}}}}}}"
                    ),
                    format_type="merge",
                )
            except CommandFailed:
                logger.warning("Failed to restore StorageCluster config")

        request.addfinalizer(finalizer)

        # 1. Patch StorageCluster with endpoint counts and KEDA autoscaler
        logger.info(
            f"Configuring StorageCluster: endpoints min={self.MIN_ENDPOINT_COUNT}, "
            f"max={self.MAX_ENDPOINT_COUNT}, autoscalerType=keda"
        )
        sc_ocp.patch(
            resource_name=sc_name,
            params=(
                f'{{"spec":{{"multiCloudGateway":{{'
                f'"endpoints":{{"minCount":{self.MIN_ENDPOINT_COUNT},"maxCount":{self.MAX_ENDPOINT_COUNT}}},'
                f'"autoscaler":{{"autoscalerType":"keda"}}'
                f"}}}}}}"
            ),
            format_type="merge",
        )

        # 2. Wait for ScaledObject creation and HPA deletion
        scaled_object_ocp = OCP(kind=constants.SCALED_OBJECT, namespace=namespace)

        def _scaled_object_exists():
            try:
                scaled_object_ocp.get(resource_name="noobaa")
                return True
            except CommandFailed:
                return False

        logger.info("Waiting for ScaledObject 'noobaa' to be created")
        try:
            for exists in TimeoutSampler(120, 10, _scaled_object_exists):
                if exists:
                    logger.info("ScaledObject created by noobaa-operator")
                    break
        except TimeoutExpiredError:
            raise TimeoutExpiredError("ScaledObject was not created")

        hpa_ocp = OCP(kind="HorizontalPodAutoscaler", namespace=namespace)

        def _hpa_deleted():
            try:
                hpa_ocp.get(resource_name="noobaa-hpav2")
                return False
            except CommandFailed:
                return True

        logger.info("Waiting for HPA 'noobaa-hpav2' to be deleted")
        try:
            for deleted in TimeoutSampler(60, 10, _hpa_deleted):
                if deleted:
                    logger.info("HPA deleted by noobaa-operator")
                    break
        except TimeoutExpiredError:
            logger.warning("HPA was not deleted, continuing anyway")

        # 3. Wait for endpoints to stabilize at minCount
        logger.info(f"Waiting for endpoints to stabilize at {self.MIN_ENDPOINT_COUNT}")
        try:
            for endpoint_pods in TimeoutSampler(
                timeout=300,
                sleep=30,
                func=get_pods_having_label,
                label=constants.NOOBAA_ENDPOINT_POD_LABEL,
                namespace=namespace,
            ):
                count = len(endpoint_pods)
                logger.info(f"Endpoint pod count: {count}")
                if count == self.MIN_ENDPOINT_COUNT:
                    break
        except TimeoutExpiredError:
            raise TimeoutExpiredError(
                f"Endpoints did not stabilize at {self.MIN_ENDPOINT_COUNT}"
            )

    @pytest.fixture(scope="class")
    def warp_workload_runner(self, request):
        """Create a WarpWorkloadRunner targeting the NooBaa S3 endpoint."""
        namespace = config.ENV_DATA["cluster_namespace"]
        host = f"s3.{namespace}.svc:443"
        return WarpWorkloadRunner(request, host)

    def test_noobaa_endpoint_keda_autoscaling(
        self,
        setup_keda_autoscaling,
        bucket_factory,
        warp_workload_runner,
    ):
        """
        Test KEDA-based autoscaling of NooBaa endpoint pods.

        1. Create an OBC and start S3 load via Warp
        2. Wait for endpoint pods to scale up
        3. Stop the workload
        4. Wait for endpoint pods to scale back down to minCount
        """
        namespace = config.ENV_DATA["cluster_namespace"]

        # 1. Create an OBC and start S3 load
        bucket = bucket_factory(amount=1, interface="OC")[0]
        obc_obj = OBC(bucket.name)
        warp_workload_runner.start(
            access_key=obc_obj.access_key_id,
            secret_key=obc_obj.access_key,
            bucket_name=bucket.name,
            workload_type="mixed",
            concurrent=32,
            obj_size="1MiB",
            duration="30s",
        )

        # 2. Wait for scale-up
        try:
            for endpoint_pods in TimeoutSampler(
                timeout=300,
                sleep=30,
                func=get_pods_having_label,
                label=constants.NOOBAA_ENDPOINT_POD_LABEL,
                namespace=namespace,
            ):
                count = len(endpoint_pods)
                pod_names = ", ".join(p["metadata"]["name"] for p in endpoint_pods)
                logger.info(f"Endpoint pods ({count}): {pod_names}")
                if count > self.MIN_ENDPOINT_COUNT:
                    logger.info("Endpoints scaled up")
                    break
        except TimeoutExpiredError:
            logger.error("Endpoints did not scale up")
            raise
        finally:
            # 3. Stop the workload
            warp_workload_runner.stop()

        # 4. Wait for scale-down
        try:
            for endpoint_pods in TimeoutSampler(
                timeout=900,
                sleep=30,
                func=get_pods_having_label,
                label=constants.NOOBAA_ENDPOINT_POD_LABEL,
                namespace=namespace,
            ):
                count = len(endpoint_pods)
                logger.info(f"Endpoint pod count: {count}")
                if count == self.MIN_ENDPOINT_COUNT:
                    logger.info("Endpoints scaled down")
                    break
        except TimeoutExpiredError:
            logger.error("Endpoints did not scale down")
            raise
