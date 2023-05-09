import pytest

from ocs_ci.framework.testlib import MCGTest
from ocs_ci.framework.pytest_customization.marks import (
    bugzilla,
    skipif_disconnected_cluster,
    skipif_proxy_cluster,
)


@skipif_disconnected_cluster
@skipif_proxy_cluster
@bugzilla("2165493")
class TestAzureUlsWithManyBlobs(MCGTest):
    @pytest.fixture(scope="class", autouse=True)
    def create_many_az_blobs(self, backingstore_factory_session, blobs_count=100):
        backingstore_factory_session(
            method="oc", uls_dict={"azure": [(blobs_count, None)]}
        )

    def test_create_az_bs(self, backingstore_factory_session):
        backingstore_factory_session(method="oc", uls_dict={"azure": [(1, None)]})

    def test_create_az_nss(self, namespace_store_factory_session):
        namespace_store_factory_session(method="oc", nss_dict={"azure": [(1, None)]})
