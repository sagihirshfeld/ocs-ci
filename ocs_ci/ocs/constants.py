"""
Constants module.

This module contains any values that are widely used across the framework,
utilities, or tests that will predominantly remain unchanged.

In the event values here have to be changed it should be under careful review
and with consideration of the entire project.

"""

import os


# Logging
LOG_FORMAT = "%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s"

# Directories
TOP_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONF_DIR = os.path.join(TOP_DIR, "conf")
FRAMEWORK_CONF_DIR = os.path.join(TOP_DIR, "ocs_ci", "framework", "conf")
OCP_VERSION_CONF_DIR = os.path.join(FRAMEWORK_CONF_DIR, "ocp_version")
OCS_VERSION_CONF_DIR = os.path.join(FRAMEWORK_CONF_DIR, "ocs_version")
TEMPLATE_DIR = os.path.join(TOP_DIR, "ocs_ci", "templates")
TEMPLATE_CLEANUP_DIR = os.path.join(TEMPLATE_DIR, "cleanup")
REPO_DIR = os.path.join(TOP_DIR, "ocs_ci", "repos")
EXTERNAL_DIR = os.path.join(TOP_DIR, "external")
TEMPLATE_DEPLOYMENT_DIR = os.path.join(TEMPLATE_DIR, "ocs-deployment")
TEMPLATE_DEPLOYMENT_DIR_LVMO = os.path.join(TEMPLATE_DIR, "lvmo-deployment")
TEMPLATE_MULTICLUSTER_DIR = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "multicluster")
TEMPLATE_CEPH_DIR = os.path.join(TEMPLATE_DIR, "ceph")
TEMPLATE_CSI_DIR = os.path.join(TEMPLATE_DIR, "CSI")
TEMPLATE_CSI_LVM_DIR = os.path.join(TEMPLATE_CSI_DIR, "lvm")
TEMPLATE_CSI_RBD_DIR = os.path.join(TEMPLATE_CSI_DIR, "rbd")
TEMPLATE_CSI_FS_DIR = os.path.join(TEMPLATE_CSI_DIR, "cephfs")
TEMPLATE_PV_PVC_DIR = os.path.join(TEMPLATE_DIR, "pv_pvc")
TEMPLATE_APP_POD_DIR = os.path.join(TEMPLATE_DIR, "app-pods")
TEMPLATE_WORKLOAD_DIR = os.path.join(TEMPLATE_DIR, "workloads")
TEMPLATE_FIO_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "fio")
TEMPLATE_SMALLFILE_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "smallfile")
TEMPLATE_PGSQL_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "pgsql")
TEMPLATE_JENKINS_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "jenkins")
TEMPLATE_PGSQL_SERVER_DIR = os.path.join(TEMPLATE_PGSQL_DIR, "server")
TEMPLATE_COUCHBASE_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "couchbase")
TEMPLATE_COUCHBASE_SERVER_DIR = os.path.join(TEMPLATE_COUCHBASE_DIR, "server")
TEMPLATE_COUCHBASE_PILLOWFIGHT_DIR = os.path.join(TEMPLATE_COUCHBASE_DIR, "pillowfight")
TEMPLATE_MCG_DIR = os.path.join(TEMPLATE_DIR, "mcg")
TEMPLATE_AMQ_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "amq")
TEMPLATE_OPENSHIFT_INFRA_DIR = os.path.join(TEMPLATE_DIR, "openshift-infra/")
TEMPLATE_HSBENCH_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "hsbench")
TEMPLATE_BDI_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "bdi")
TEMPLATE_OSD_SCALE_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "osd_scale")
TEMPLATE_CONFIGURE_PVC_MONITORING_POD = os.path.join(
    TEMPLATE_OPENSHIFT_INFRA_DIR, "monitoring/"
)
TEMPLATE_DEPLOYMENT_LOGGING = os.path.join(
    TEMPLATE_OPENSHIFT_INFRA_DIR, "logging-deployment"
)
TEMPLATE_DEPLOYMENT_EO = os.path.join(
    TEMPLATE_DEPLOYMENT_LOGGING, "elasticsearch_operator"
)
TEMPLATE_DEPLOYMENT_CLO = os.path.join(
    TEMPLATE_DEPLOYMENT_LOGGING, "clusterlogging_operator"
)
TEMPLATE_AUTHENTICATION_DIR = os.path.join(TEMPLATE_DIR, "authentication")
DATA_DIR = os.path.join(TOP_DIR, "data")
ROOK_REPO_DIR = os.path.join(DATA_DIR, "rook")
ROOK_EXAMPLES_DIR = os.path.join(
    ROOK_REPO_DIR, "cluster", "examples", "kubernetes", "ceph"
)
ROOK_CSI_RBD_DIR = os.path.join(ROOK_EXAMPLES_DIR, "csi", "rbd")
ROOK_CSI_CEPHFS_DIR = os.path.join(ROOK_EXAMPLES_DIR, "csi", "cephfs")
CLEANUP_YAML = "cleanup.yaml.j2"
MANIFESTS_DIR = "manifests"

# OCP Deployment constants
CHRONY_TEMPLATE = os.path.join(
    TEMPLATE_DIR, "ocp-deployment", "99-role-chrony-configuration.yaml"
)
HUGE_PAGES_TEMPLATE = os.path.join(TEMPLATE_DIR, "ocp-deployment", "huge_pages.yaml")
NAMESPACE_TEMPLATE = os.path.join(TEMPLATE_DIR, "ocp-deployment", "namespace.yaml")
# Statuses
STATUS_READY = "Ready"
STATUS_PENDING = "Pending"
STATUS_CONTAINER_CREATING = "ContainerCreating"
STATUS_AVAILABLE = "Available"
STATUS_RUNNING = "Running"
STATUS_TERMINATING = "Terminating"
STATUS_CLBO = "CrashLoopBackOff"
STATUS_BOUND = "Bound"
STATUS_RELEASED = "Released"
STATUS_COMPLETED = "Completed"
STATUS_ERROR = "Error"
STATUS_READYTOUSE = "READYTOUSE"
STATUS_FAILED = "Failed"
STATUS_FAILEDOVER = "FailedOver"
STATUS_RELOCATED = "Relocated"

# NooBaa statuses
BS_AUTH_FAILED = "AUTH_FAILED"
BS_OPTIMAL = "OPTIMAL"
HEALTHY_OB = "OPTIMAL"
HEALTHY_OBC = STATUS_BOUND
HEALTHY_OBC_CLI_PHASE = "Phase:Bound"
HEALTHY_OB_CLI_MODE = "Mode:OPTIMAL"
HEALTHY_PV_BS = ["`OPTIMAL`", "`LOW_CAPACITY`"]

# Resources / Kinds
CEPHFILESYSTEM = "CephFileSystem"
CEPHBLOCKPOOL = "CephBlockPool"
CEPHBLOCKPOOL_THICK = "CephBlockPoolThick"
CEPHBLOCKPOOL_SC = "ocs-storagecluster-ceph-rbd"
CEPHFILESYSTEM_SC = "ocs-storagecluster-cephfs"
LVM_SC = "odf-lvm-vg1"
NOOBAA_SC = "openshift-storage.noobaa.io"
LOCALSTORAGE_SC = "localblock"
DEPLOYMENT = "Deployment"
STORAGECLASS = "StorageClass"
STORAGESYSTEM = "StorageSystem"
PV = "PersistentVolume"
PVC = "PersistentVolumeClaim"
POD = "Pod"
ROUTE = "Route"
SERVICE = "Service"
NODE = "Node"
DEPLOYMENTCONFIG = "deploymentconfig"
CONFIG = "Config"
CONFIGMAP = "ConfigMap"
MACHINESETS = "machinesets"
STORAGECLUSTER = "storagecluster"
CLUSTER_OPERATOR = "ClusterOperator"
MONITORING = "monitoring"
CLUSTER_SERVICE_VERSION = "csv"
JOB = "job"
OAUTH = "OAuth"
LOCAL_VOLUME = "localvolume"
PROXY = "Proxy"
MACHINECONFIGPOOL = "MachineConfigPool"
VOLUMESNAPSHOTCLASS = "VolumeSnapshotClass"
HPA = "horizontalpodautoscaler"
VOLUMESNAPSHOTCONTENT = "VolumeSnapshotContent"
POD_DISRUPTION_BUDGET = "PodDisruptionBudget"
STATEFULSET = "StatefulSet"
BACKINGSTORE = "Backingstore"
NAMESPACESTORE = "Namespacestore"
BUCKETCLASS = "Bucketclass"
DRPC = "DRPlacementControl"
CEPHFILESYSTEMSUBVOLUMEGROUP = "cephfilesystemsubvolumegroup"
CATSRC = "catsrc"
VOLUME_REPLICATION = "VolumeReplication"
RECLAIMSPACECRONJOB = "reclaimspacecronjob"
LVMCLUSTER = "lvmcluster"

# Provisioners
AWS_EFS_PROVISIONER = "openshift.org/aws-efs"
ROLE = "Role"
ROLEBINDING = "Rolebinding"
SUBSCRIPTION = "Subscription"
NAMESPACES = "Namespaces"
CLUSTER_LOGGING = "ClusterLogging"
OPERATOR_GROUP = "OperatorGroup"
SERVICE_ACCOUNT = "Serviceaccount"
SCC = "SecurityContextConstraints"
PRIVILEGED = "privileged"
ANYUID = "anyuid"
OCSINITIALIZATION = "OCSInitialization"
OCSINIT = "ocsinit"

# Other
SECRET = "Secret"
TEST = "test"
NAMESPACE = "Namespace"
IGNORE_SC_GP2 = "gp2"
IGNORE_SC_FLEX = "rook-ceph-block"
TEST_FILES_BUCKET = "ocsci-test-files"
ROOK_REPOSITORY = "https://github.com/rook/rook.git"
OPENSHIFT_STORAGE_NAMESPACE = "openshift-storage"
OPENSHIFT_MACHINE_API_NAMESPACE = "openshift-machine-api"
OPENSHIFT_LOGGING_NAMESPACE = "openshift-logging"
OPENSHIFT_OPERATORS_REDHAT_NAMESPACE = "openshift-operators-redhat"
OPENSHIFT_IMAGE_REGISTRY_NAMESPACE = "openshift-image-registry"
OPENSHIFT_IMAGE_REGISTRY_DEPLOYMENT = "image-registry"
OPENSHIFT_IMAGE_SELECTOR = "docker-registry=default"
OPENSHIFT_INGRESS_NAMESPACE = "openshift-ingress"
OPENSHIFT_MONITORING_NAMESPACE = "openshift-monitoring"
MASTER_MACHINE = "master"
WORKER_MACHINE = "worker"
BOOTSTRAP_MACHINE = "bootstrap"
INFRA_MACHINE = "infra"
MOUNT_POINT = "/var/lib/www/html"
TOLERATION_KEY = "node.ocs.openshift.io/storage"

OCP_QE_MISC_REPO = "https://gitlab.cee.redhat.com/aosqe/flexy-templates.git"
CRITICAL_ERRORS = ["core dumped", "oom_reaper"]
must_gather_pod_label = "must-gather"
drain_canary_pod_label = "rook-ceph-drain-canary"
OCS_MONKEY_REPOSITORY = "https://github.com/red-hat-storage/ocs-monkey.git"

# AMQ
AMQ_NAMESPACE = "myproject"
KAFKA_OPERATOR = "https://github.com/strimzi/strimzi-kafka-operator"
RGW_KAFKA_NOTIFY = "https://github.com/shonpaz123/notify/"
OCS_WORKLOADS = "https://github.com/red-hat-storage/ocs-workloads"
CODESPEED_URL = "http://10.0.78.167:8000/"

UPI_INSTALL_SCRIPT = "upi_on_aws-install.sh"

DEFAULT_CLUSTERNAME = "ocs-storagecluster"
DEFAULT_CLUSTERNAME_EXTERNAL_MODE = "ocs-external-storagecluster"
DEFAULT_BLOCKPOOL = f"{DEFAULT_CLUSTERNAME}-cephblockpool"
METADATA_POOL = f"{DEFAULT_CLUSTERNAME}-cephfilesystem-metadata"
DATA_POOL = f"{DEFAULT_CLUSTERNAME}-cephfilesystem-data0"
DEFAULT_ROUTE_CRT = "router-certs-default"
DEFAULT_NAMESPACE = "default"
IMAGE_REGISTRY_RESOURCE_NAME = "cluster"
IMAGE_REGISTRY_CONFIG = "configs.imageregistry.operator.openshift.io/cluster"
DEFAULT_NOOBAA_BACKINGSTORE = "noobaa-default-backing-store"
DEFAULT_NOOBAA_BUCKETCLASS = "noobaa-default-bucket-class"
NOOBAA_RESOURCE_NAME = "noobaa"
MIN_PV_BACKINGSTORE_SIZE_IN_GB = 17
JENKINS_BUILD = "jax-rs-build"
JENKINS_BUILD_COMPLETE = "Complete"
RIPSAW_DROP_CACHE = os.path.join(TEMPLATE_FIO_DIR, "drop_cache_pod.yaml")
OCP_QE_DEVICEPATH_REPO = "https://github.com/anubhav-here/device-by-id-ocp.git"

# Default pools
DEFAULT_CEPHBLOCKPOOL = "ocs-storagecluster-cephblockpool"
# Default StorageClass
DEFAULT_STORAGECLASS_CEPHFS = f"{DEFAULT_CLUSTERNAME}-cephfs"
DEFAULT_STORAGECLASS_RBD = f"{DEFAULT_CLUSTERNAME}-ceph-rbd"
DEFAULT_STORAGECLASS_RGW = f"{DEFAULT_CLUSTERNAME}-ceph-rgw"
DEFAULT_STORAGECLASS_RBD_THICK = f"{DEFAULT_CLUSTERNAME}-ceph-rbd-thick"

# Independent mode default StorageClasses
DEFAULT_EXTERNAL_MODE_STORAGECLASS_RGW = f"{DEFAULT_CLUSTERNAME_EXTERNAL_MODE}-ceph-rgw"

# Default StorageClass for External-mode
DEFAULT_EXTERNAL_MODE_STORAGECLASS_CEPHFS = (
    f"{DEFAULT_CLUSTERNAME_EXTERNAL_MODE}-cephfs"
)
DEFAULT_EXTERNAL_MODE_STORAGECLASS_RBD = f"{DEFAULT_CLUSTERNAME_EXTERNAL_MODE}-ceph-rbd"
DEFAULT_EXTERNAL_MODE_STORAGECLASS_RBD_THICK = (
    f"{DEFAULT_CLUSTERNAME_EXTERNAL_MODE}-ceph-rbd-thick"
)

# Default VolumeSnapshotClass
DEFAULT_VOLUMESNAPSHOTCLASS_CEPHFS = f"{DEFAULT_CLUSTERNAME}-cephfsplugin-snapclass"
DEFAULT_VOLUMESNAPSHOTCLASS_RBD = f"{DEFAULT_CLUSTERNAME}-rbdplugin-snapclass"
DEFAULT_VOLUMESNAPSHOTCLASS_LVM = "odf-lvm-vg1"
DEFAULT_EXTERNAL_MODE_VOLUMESNAPSHOTCLASS_CEPHFS = (
    f"{DEFAULT_CLUSTERNAME_EXTERNAL_MODE}-cephfsplugin-snapclass"
)
DEFAULT_EXTERNAL_MODE_VOLUMESNAPSHOTCLASS_RBD = (
    f"{DEFAULT_CLUSTERNAME_EXTERNAL_MODE}-rbdplugin-snapclass"
)

# encoded value of 'admin'
ADMIN_USER = "admin"
GB = 1024**3
GB2KB = 1024**2
GB2MB = 1024

# Reclaim Policy
RECLAIM_POLICY_RETAIN = "Retain"
RECLAIM_POLICY_DELETE = "Delete"

# Access Mode
ACCESS_MODE_RWO = "ReadWriteOnce"
ACCESS_MODE_ROX = "ReadOnlyMany"
ACCESS_MODE_RWX = "ReadWriteMany"
ACCESS_MODE_RWOP = "ReadWriteOncePod"

# Pod names
NB_DB_NAME_46_AND_BELOW = "noobaa-db-0"
NB_DB_NAME_47_AND_ABOVE = "noobaa-db-pg-0"

# Pod label
MON_APP_LABEL = "app=rook-ceph-mon"
MDS_APP_LABEL = "app=rook-ceph-mds"
CRASHCOLLECTOR_APP_LABEL = "app=rook-ceph-crashcollector"
TOOL_APP_LABEL = "app=rook-ceph-tools"
MGR_APP_LABEL = "app=rook-ceph-mgr"
OSD_APP_LABEL = "app=rook-ceph-osd"
OSD_PREPARE_APP_LABEL = "app=rook-ceph-osd-prepare"
RGW_APP_LABEL = "app=rook-ceph-rgw"
OPERATOR_LABEL = "app=rook-ceph-operator"
CSI_CEPHFSPLUGIN_PROVISIONER_LABEL = "app=csi-cephfsplugin-provisioner"
CSI_RBDPLUGIN_PROVISIONER_LABEL = "app=csi-rbdplugin-provisioner"
CSI_CEPHFSPLUGIN_LABEL = "app=csi-cephfsplugin"
CSI_RBDPLUGIN_LABEL = "app=csi-rbdplugin"
OCS_OPERATOR_LABEL = "name=ocs-operator"
ODF_OPERATOR_CONTROL_MANAGER_LABEL = "control-plane=controller-manager"
ROOK_CEPH_DRAIN_CANARY = "rook-ceph-drain-canary"
LOCAL_STORAGE_OPERATOR_LABEL = "name=local-storage-operator"
NOOBAA_APP_LABEL = "app=noobaa"
NOOBAA_CORE_POD_LABEL = "noobaa-core=noobaa"
NOOBAA_OPERATOR_POD_LABEL = "noobaa-operator=deployment"
NOOBAA_DB_LABEL_46_AND_UNDER = "noobaa-db=noobaa"
NOOBAA_DB_LABEL_47_AND_ABOVE = "noobaa-db=postgres"
NOOBAA_ENDPOINT_POD_LABEL = "noobaa-s3=noobaa"
ROOK_CEPH_DETECT_VERSION_LABEL = "app=rook-ceph-detect-version"
CEPH_FILE_CONTROLLER_DETECT_VERSION_LABEL = "app=ceph-file-controller-detect-version"
CEPH_OBJECT_CONTROLLER_DETECT_VERSION_LABEL = (
    "app=ceph-object-controller-detect-version"
)
DEFAULT_DEVICESET_PVC_NAME = "ocs-deviceset"
DEFAULT_DEVICESET_LSO_PVC_NAME = "ocs-deviceset-localblock"
DEFAULT_MON_PVC_NAME = "rook-ceph-mon"
OSD_PVC_GENERIC_LABEL = "ceph.rook.io/DeviceSet"
CEPH_ROOK_IO_PVC_LABEL = "ceph.rook.io/pvc"
ROOK_CEPH_MON_PVC_LABEL = "pvc_name"
PGSQL_APP_LABEL = "app=postgres"
HOSTNAME_LABEL = "kubernetes.io/hostname"
OCS_METRICS_EXPORTER = "app.kubernetes.io/name=ocs-metrics-exporter"
MANAGED_PROMETHEUS_LABEL = "prometheus=managed-ocs-prometheus"
MANAGED_ALERTMANAGER_LABEL = "alertmanager=managed-ocs-alertmanager"
MANAGED_CONTROLLER_LABEL = "control-plane=controller-manager"
PROVIDER_SERVER_LABEL = "app=ocsProviderApiServer"
PROMETHEUS_OPERATOR_LABEL = "app.kubernetes.io/name=prometheus-operator"

# Noobaa Deployments and Statefulsets
NOOBAA_OPERATOR_DEPLOYMENT = "noobaa-operator"
NOOBAA_ENDPOINT_DEPLOYMENT = "noobaa-endpoint"
NOOBAA_DB_STATEFULSET = "noobaa-db-pg"
NOOBAA_CORE_STATEFULSET = "noobaa-core"

# Auth Yaml
OCSCI_DATA_BUCKET = "ocs-ci-data"
AUTHYAML = "auth.yaml"
GOOGLE_CREDS_JSON_PATH = os.path.join(DATA_DIR, "google_creds.json")

# OBJ File representing serialized data
NODE_OBJ_FILE = "node_file.objs"
NODE_FILE = "nodes.objs"
INSTANCE_FILE = "instances.objs"

# Ceph keyring template
CEPH_KEYRING = "ceph-keyring.j2"

# YAML paths
TOOL_POD_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "toolbox_pod.yaml")

CEPHFILESYSTEM_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "CephFileSystem.yaml")

CEPHBLOCKPOOL_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "cephblockpool.yaml")

VSPHERE_THICK_STORAGECLASS_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "vsphere_storageclass_thick.yaml"
)

CSI_RBD_STORAGECLASS_YAML = os.path.join(TEMPLATE_CSI_RBD_DIR, "storageclass.yaml")

ROOK_CSI_RBD_STORAGECLASS_YAML = os.path.join(ROOK_CSI_RBD_DIR, "storageclass.yaml")

CSI_RBD_PVC_CLONE_YAML = os.path.join(TEMPLATE_CSI_RBD_DIR, "pvc-clone.yaml")

CSI_CEPHFS_STORAGECLASS_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "storageclass.yaml")

CSI_CEPHFS_PVC_CLONE_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "pvc-clone.yaml")

CSI_LVM_STORAGECLASS_YAML = os.path.join(TEMPLATE_CSI_LVM_DIR, "storageclass.yaml")

ROOK_CSI_CEPHFS_STORAGECLASS_YAML = os.path.join(
    ROOK_CSI_CEPHFS_DIR, "storageclass.yaml"
)

WFFC_VOLUMEBINDINGMODE = "WaitForFirstConsumer"

IMMEDIATE_VOLUMEBINDINGMODE = "Immediate"

CSI_PVC_YAML = os.path.join(TEMPLATE_PV_PVC_DIR, "PersistentVolumeClaim.yaml")

MCG_OBC_YAML = os.path.join(TEMPLATE_MCG_DIR, "ObjectBucketClaim.yaml")

RGW_OBC_YAML = os.path.join(TEMPLATE_MCG_DIR, "ObjectBucketClaim-RGW.yaml")

MCG_AWS_CREDS_YAML = os.path.join(TEMPLATE_MCG_DIR, "AwsCreds.yaml")

MCG_BACKINGSTORE_SECRET_YAML = os.path.join(TEMPLATE_MCG_DIR, "BackingStoreSecret.yaml")

MCG_BACKINGSTORE_YAML = os.path.join(TEMPLATE_MCG_DIR, "BackingStore.yaml")

MCG_NAMESPACESTORE_YAML = os.path.join(TEMPLATE_MCG_DIR, "NamespaceStore.yaml")

PV_BACKINGSTORE_YAML = os.path.join(TEMPLATE_MCG_DIR, "PVBackingStore.yaml")

MCG_BUCKETCLASS_YAML = os.path.join(TEMPLATE_MCG_DIR, "BucketClass.yaml")

CSI_RBD_POD_YAML = os.path.join(TEMPLATE_CSI_RBD_DIR, "pod.yaml")

CSI_RBD_RAW_BLOCK_POD_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "raw_block_pod.yaml")

CSI_CEPHFS_POD_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "pod.yaml")
CSI_RBD_SECRET_YAML = os.path.join(TEMPLATE_CSI_RBD_DIR, "secret.yaml")

CSI_CEPHFS_SECRET_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "secret.yaml")

CSI_CEPHFS_PVC_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "pvc.yaml")

CSI_CEPHFS_PVC_RESTORE_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "pvc-restore.yaml")

CSI_LVM_PVC_RESTORE_YAML = os.path.join(TEMPLATE_CSI_LVM_DIR, "restore-pvc.yaml")

CSI_CEPHFS_SNAPSHOT_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "snapshot.yaml")

CSI_LVM_SNAPSHOT_YAML = os.path.join(TEMPLATE_CSI_LVM_DIR, "volume-snapshot.yaml")

CSI_CEPHFS_SNAPSHOTCLASS_YAML = os.path.join(TEMPLATE_CSI_FS_DIR, "snapshotclass.yaml")

CSI_RBD_PVC_YAML = os.path.join(TEMPLATE_CSI_RBD_DIR, "pvc.yaml")

CSI_RBD_PVC_RESTORE_YAML = os.path.join(TEMPLATE_CSI_RBD_DIR, "pvc-restore.yaml")

CSI_RBD_SNAPSHOT_YAML = os.path.join(TEMPLATE_CSI_RBD_DIR, "snapshot.yaml")

CSI_RBD_SNAPSHOTCLASS_YAML = os.path.join(TEMPLATE_CSI_RBD_DIR, "snapshotclass.yaml")

CONFIGURE_PVC_ON_MONITORING_POD = os.path.join(
    TEMPLATE_CONFIGURE_PVC_MONITORING_POD, "configuring_pvc.yaml"
)

FIO_CR_YAML = os.path.join(TEMPLATE_FIO_DIR, "benchmark_fio.yaml")

PGSQL_SERVICE_YAML = os.path.join(TEMPLATE_PGSQL_SERVER_DIR, "Service.yaml")

PGSQL_CONFIGMAP_YAML = os.path.join(TEMPLATE_PGSQL_SERVER_DIR, "ConfigMap.yaml")

PGSQL_STATEFULSET_YAML = os.path.join(TEMPLATE_PGSQL_SERVER_DIR, "StatefulSet.yaml")

PGSQL_BENCHMARK_YAML = os.path.join(TEMPLATE_PGSQL_DIR, "PGSQL_Benchmark.yaml")

JENKINS_BUILDCONFIG_YAML = os.path.join(TEMPLATE_JENKINS_DIR, "buildconfig.yaml")

SMALLFILE_BENCHMARK_YAML = os.path.join(TEMPLATE_SMALLFILE_DIR, "SmallFile.yaml")

OSD_SCALE_BENCHMARK_YAML = os.path.join(
    TEMPLATE_OSD_SCALE_DIR, "osd_scale_benchmark.yaml"
)

COUCHBASE_OPERATOR_GROUP_YAML = os.path.join(
    TEMPLATE_COUCHBASE_SERVER_DIR, "cb-operatorgroup.yaml"
)

COUCHBASE_OPERATOR_SUBSCRIPTION_YAML = os.path.join(
    TEMPLATE_COUCHBASE_SERVER_DIR, "cb-subscription.yaml"
)

COUCHBASE_WORKER_SECRET = os.path.join(
    TEMPLATE_COUCHBASE_SERVER_DIR, "couchbase-worker-secret.yaml"
)

COUCHBASE_WORKER_EXAMPLE = os.path.join(
    TEMPLATE_COUCHBASE_SERVER_DIR, "couchbase-worker.yaml"
)

COUCHBASE_DATA_BUCKET = os.path.join(
    TEMPLATE_COUCHBASE_SERVER_DIR, "couchbase-data-bucket.yaml"
)

COUCHBASE_PILLOWFIGHT = os.path.join(
    TEMPLATE_COUCHBASE_PILLOWFIGHT_DIR, "basic-pillowfight.yaml"
)

COUCHBASE_OPERATOR = "couchbase-operator-namespace"

KAFKADROP_YAML = os.path.join(TEMPLATE_AMQ_DIR, "kafkadrop.yaml")

HELLO_WORLD_PRODUCER_YAML = os.path.join(TEMPLATE_AMQ_DIR, "hello-world-producer.yaml")

HELLO_WORLD_CONSUMER_YAML = os.path.join(TEMPLATE_AMQ_DIR, "hello-world-consumer.yaml")

AMQ_RBAC_YAML = os.path.join(TEMPLATE_AMQ_DIR, "rbac.yaml")

AMQ_BENCHMARK_POD_YAML = os.path.join(TEMPLATE_AMQ_DIR, "benchmark")

AMQ_BENCHMARK_VALUE_YAML = os.path.join(AMQ_BENCHMARK_POD_YAML, "values.yaml")

AMQ_DRIVER_KAFKA_YAML = os.path.join(TEMPLATE_AMQ_DIR, "driver-kafka.yaml")

AMQ_WORKLOAD_YAML = os.path.join(TEMPLATE_AMQ_DIR, "amq_workload.yaml")

AMQ_SIMPLE_WORKLOAD_YAML = os.path.join(TEMPLATE_AMQ_DIR, "amq_simple_workload.yaml")

KAFKA_ENDPOINT = f"my-cluster-kafka-bootstrap.{AMQ_NAMESPACE}.svc.cluster.local:9092"

NGINX_POD_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "nginx.yaml")

PERF_POD_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "performance.yaml")

PERF_BLOCK_POD_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "performance_block.yaml")

HSBENCH_OBJ_YAML = os.path.join(TEMPLATE_HSBENCH_DIR, "hsbench_obj.yaml")

IBM_BDI_SCC_WORKLOAD_YAML = os.path.join(TEMPLATE_BDI_DIR, "ibm_bdi_scc.yaml")

TILLER_YAML = os.path.join(TEMPLATE_BDI_DIR, "temp_tiller.yaml")

IBM_BDI_CONFIGURE_WORKLOAD_YAML = os.path.join(
    TEMPLATE_BDI_DIR, "configure-workload.yaml"
)

IBM_BDI_DATA_LOAD_WORKLOAD_YAML = os.path.join(TEMPLATE_BDI_DIR, "data-load-job.yaml")

IBM_BDI_RUN_WORKLOAD_YAML = os.path.join(TEMPLATE_BDI_DIR, "run-workload.yaml")

AWSCLI_SERVICE_CA_YAML = os.path.join(
    TEMPLATE_MCG_DIR, "aws-cli-service-ca-configmap.yaml"
)

AWSCLI_POD_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "awscli.yaml")

AWSCLI_MULTIARCH_POD_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "awscli_multiarch.yaml")

NSFS_INTERFACE_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "ubi8.yaml")

SERVICE_ACCOUNT_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "service_account.yaml")

SERVICE_ACCOUNT_TOKEN_SECRET = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "serviceaccount_token_secret.yaml"
)

FEDORA_DC_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "fedora_dc.yaml")

RHEL_7_7_POD_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "rhel-7_7.yaml")

GOLANG_YAML = os.path.join(TEMPLATE_APP_POD_DIR, "golang.yaml")

CSI_RBD_RECLAIM_SPACE_JOB_YAML = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "reclaimspacejob.yaml"
)

CSI_RBD_RECLAIM_SPACE_CRONJOB_YAML = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "reclaimspacecronjob.yaml"
)

OC_MIRROR_IMAGESET_CONFIG = os.path.join(
    TEMPLATE_DIR, "ocp-deployment", "oc-mirror-imageset-config.yaml"
)

# Openshift-logging elasticsearch operator deployment yamls
EO_NAMESPACE_YAML = os.path.join(TEMPLATE_DEPLOYMENT_EO, "eo-project.yaml")

EO_OG_YAML = os.path.join(TEMPLATE_DEPLOYMENT_EO, "eo-og.yaml")
EO_RBAC_YAML = os.path.join(TEMPLATE_DEPLOYMENT_EO, "eo-rbac.yaml")
EO_SUB_YAML = os.path.join(TEMPLATE_DEPLOYMENT_EO, "eo-sub.yaml")

OLM_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "deploy-with-olm.yaml")

CATALOG_SOURCE_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "catalog-source.yaml")

OCS_SECRET_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "ocs-secret.yaml")

STAGE_IMAGE_CONTENT_SOURCE_POLICY_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "stageImageContentSourcePolicy.yaml"
)

SUBSCRIPTION_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "subscription.yaml")

SUBSCRIPTION_ODF_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "subscription_odf.yaml")

STORAGE_CLUSTER_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "storage-cluster.yaml")

STORAGE_SYSTEM_ODF_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "storagesystem_odf.yaml"
)

EXTERNAL_STORAGE_CLUSTER_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "external-storage-cluster.yaml"
)

EXTERNAL_CLUSTER_SECRET_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "external-cluster-secret.yaml"
)

OPERATOR_SOURCE_SECRET_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "operator-source-secret.yaml"
)

OPERATOR_SOURCE_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "operator-source.yaml")

HTPASSWD_IDP_YAML = os.path.join(TEMPLATE_AUTHENTICATION_DIR, "htpasswd_provider.yaml")

IBM_COS_SECRET_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "ibm-cloud-secret.yaml")
OCS_OPERATOR_CSV_YAML = "ocs-operator.clusterserviceversion.yaml"

TEMPLATE_IMAGE_CONTENT_SOURCE_POLICY_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "imageContentSourcePolicy-template.yaml"
)

MULTUS_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "multus.yaml")

OPERATOR_SOURCE_NAME = "ocs-operatorsource"

OPERATOR_SOURCE_SECRET_NAME = "ocs-operatorsource-secret"

# Openshift-logging clusterlogging operator deployment yamls
CL_NAMESPACE_YAML = os.path.join(TEMPLATE_DEPLOYMENT_CLO, "cl-namespace.yaml")
CL_OG_YAML = os.path.join(TEMPLATE_DEPLOYMENT_CLO, "cl-og.yaml")
CL_SUB_YAML = os.path.join(TEMPLATE_DEPLOYMENT_CLO, "cl-sub.yaml")
CL_INSTANCE_YAML = os.path.join(TEMPLATE_DEPLOYMENT_CLO, "instance.yaml")

# Workload-io yamls
FIO_IO_PARAMS_YAML = os.path.join(TEMPLATE_FIO_DIR, "workload_io.yaml")
FIO_IO_RW_PARAMS_YAML = os.path.join(TEMPLATE_FIO_DIR, "workload_io_rw.yaml")
FIO_IO_FILLUP_PARAMS_YAML = os.path.join(TEMPLATE_FIO_DIR, "workload_io_fillup.yaml")
FIO_DC_YAML = os.path.join(TEMPLATE_FIO_DIR, "fio_dc.yaml")

# fio configuration files
FIO_S3 = os.path.join(TEMPLATE_FIO_DIR, "config_s3.fio")

# Openshift infra yamls:
RSYNC_POD_YAML = os.path.join(TEMPLATE_OPENSHIFT_INFRA_DIR, "rsync-pod.yaml")
MACHINESET_YAML = os.path.join(TEMPLATE_OPENSHIFT_INFRA_DIR, "machine-set.yaml")
MACHINESET_YAML_AZURE = os.path.join(
    TEMPLATE_OPENSHIFT_INFRA_DIR, "machineset-azure.yaml"
)
MACHINESET_YAML_RHV = os.path.join(TEMPLATE_OPENSHIFT_INFRA_DIR, "machineset-rhv.yaml")
MACHINESET_YAML_VMWARE = os.path.join(
    TEMPLATE_OPENSHIFT_INFRA_DIR, "machineset-vmware.yaml"
)
PODS_PER_NODE_COUNT_YAML = os.path.join(
    TEMPLATE_OPENSHIFT_INFRA_DIR, "max-pods-per-node.yaml"
)

ANSIBLE_INVENTORY_YAML = os.path.join("ocp-deployment", "inventory.yaml.j2")

# External vault kms yamls
EXTERNAL_VAULT_TEMPLATES = os.path.join(TEMPLATE_OPENSHIFT_INFRA_DIR, "vault")
EXTERNAL_VAULT_CA_CERT = os.path.join(
    EXTERNAL_VAULT_TEMPLATES, "ocs-kms-ca-secret.yaml"
)
EXTERNAL_VAULT_CLIENT_CERT = os.path.join(
    EXTERNAL_VAULT_TEMPLATES, "ocs-kms-client-cert.yaml"
)
EXTERNAL_VAULT_CLIENT_KEY = os.path.join(
    EXTERNAL_VAULT_TEMPLATES, "ocs-kms-client-key.yaml"
)
EXTERNAL_VAULT_KMS_TOKEN = os.path.join(EXTERNAL_VAULT_TEMPLATES, "ocs-kms-token.yaml")
EXTERNAL_VAULT_KMS_CONNECTION_DETAILS = os.path.join(
    EXTERNAL_VAULT_TEMPLATES, "ocs-kms-connection-details.yaml"
)
EXTERNAL_VAULT_CSI_KMS_TOKEN = os.path.join(TEMPLATE_CSI_RBD_DIR, "csi-kms-secret.yaml")
EXTERNAL_VAULT_CSI_KMS_CONNECTION_DETAILS = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "csi-kms-connection-details.yaml"
)
RBD_CSI_VAULT_TOKEN_REVIEWER = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "rbd-csi-vault-token-reviewer.yaml"
)
RBD_CSI_VAULT_TENANT_SA = os.path.join(TEMPLATE_CSI_RBD_DIR, "tenant-sa.yaml")
RBD_CSI_VAULT_TENANT_CONFIGMAP = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "tenant-vault-configmap.yaml"
)
CEPH_CONFIG_DEBUG_LOG_LEVEL_CONFIGMAP = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "ceph-debug-log-level-configmap.yaml"
)
# External hpcs kms yamls
EXTERNAL_HPCS_TEMPLATES = os.path.join(TEMPLATE_OPENSHIFT_INFRA_DIR, "hpcs")
EXTERNAL_HPCS_KMS_CONNECTION_DETAILS = os.path.join(
    EXTERNAL_HPCS_TEMPLATES, "ocs-kms-connection-details.yaml"
)
EXTERNAL_HPCS_CSI_KMS_CONNECTION_DETAILS = os.path.join(
    TEMPLATE_CSI_RBD_DIR, "csi-kms-connection-details-hpcs.yaml"
)
EXTERNAL_IBM_KP_KMS_SECRET = os.path.join(
    EXTERNAL_HPCS_TEMPLATES, "ibm-kp-kms-secret.yaml"
)
# Multicluster related yamls
ODF_MULTICLUSTER_ORCHESTRATOR = os.path.join(
    TEMPLATE_MULTICLUSTER_DIR, "odf_multicluster_orchestrator.yaml"
)
ODF_ORCHESTRATOR_OPERATOR_GROUP = os.path.join(
    TEMPLATE_MULTICLUSTER_DIR, "odf_orchestrator_operatorgroup.yaml"
)
MIRROR_PEER = os.path.join(TEMPLATE_MULTICLUSTER_DIR, "mirror_peer.yaml")
VOLUME_REPLICATION_CLASS = os.path.join(
    TEMPLATE_MULTICLUSTER_DIR, "volume_replication_class.yaml"
)
OPENSHIFT_DR_CLUSTER_OPERATOR = os.path.join(
    TEMPLATE_MULTICLUSTER_DIR, "openshift_dr_cluster_operator.yaml"
)
OPENSHIFT_DR_HUB_OPERATOR = os.path.join(
    TEMPLATE_MULTICLUSTER_DIR, "openshift_dr_hub_operator.yaml"
)
OPENSHIFT_DR_SYSTEM_NAMESPACE_YAML = os.path.join(
    TEMPLATE_MULTICLUSTER_DIR, "openshift_dr_system.yaml"
)
OPENSHIFT_DR_SYSTEM_OPERATORGROUP = os.path.join(
    TEMPLATE_MULTICLUSTER_DIR, "openshift_dr_system_operatorgroup.yaml"
)
DR_POLICY_ACM_HUB = os.path.join(TEMPLATE_MULTICLUSTER_DIR, "dr_policy_acm_hub.yaml")
ODR_S3_SECRET_YAML = os.path.join(TEMPLATE_MULTICLUSTER_DIR, "odr_s3_secret.yaml")
OPENSHIFT_DR_SYSTEM_NAMESPACE = "openshift-dr-system"
DR_AWS_S3_PROFILE_YAML = os.path.join(
    TEMPLATE_MULTICLUSTER_DIR, "dr_aws_s3_profile.yaml"
)
DR_RAMEN_HUB_OPERATOR_CONFIG = "ramen-hub-operator-config"
DR_RAMEN_CLUSTER_OPERATOR_CONFIG = "ramen-dr-cluster-operator-config"
ODF_MULTICLUSTER_ORCHESTRATOR_CONTROLLER_MANAGER = "odfmo-controller-manager"
RDR_MODE = "regional-dr"

# DR constants
SUBMARINER_DOWNLOAD_URL = "https://get.submariner.io"
DR_DEFAULT_NAMESPACE = "openshift-dr-systems"
TOKEN_EXCHANGE_AGENT_LABEL = "app=token-exchange-agent"
RBD_MIRRORING_STORAGECLUSTER_PATCH = (
    "-n openshift-storage --type json --patch  "
    "'[{ 'op': 'replace', 'path': '/spec/mirroring', 'value': {'enabled': true} }]'"
)
RBD_MIRRORING_ENABLED_QUERY = (
    "-o=jsonpath='{.items[?"
    "(@.metadata.ownerReferences[*].kind=='StorageCluster')].spec.mirroring.enabled}'"
)
RBD_SIDECAR_PATCH_CMD = (
    ' \'[{ "op": "add", "path": "/data/CSI_ENABLE_OMAP_GENERATOR", "value": "true" },'
    '{ "op": "add", "path": "/data/CSI_ENABLE_VOLUME_REPLICATION", "value": "true" }]\''
)
RBD_SIDECAR_COUNT = 18
DR_S3_SECRET_NAME_PREFIX = "odr-s3secret"
DR_WORKLOAD_REPO_BASE_DIR = "ocm-ramen-samples"
DR_RAMEN_CONFIG_MANAGER_KEY = "ramen_manager_config.yaml"

# constants
RBD_INTERFACE = "rbd"
CEPHFS_INTERFACE = "cephfs"
RAW_BLOCK_DEVICE = "/dev/rbdblock"

# Constant values for IOPS and Throughput is set
# considering gp2 interface, EBS volumes and EC2 instances
IOPS_FOR_1TiB_OSD = 3000
THROUGHPUT_LIMIT_OSD = 250

# EC2 instance statuses
INSTANCE_PENDING = 0
INSTANCE_STOPPING = 64
INSTANCE_STOPPED = 80
INSTANCE_RUNNING = 16
INSTANCE_SHUTTING_DOWN = 32
INSTANCE_TERMINATED = 48

# vSphere VM power statuses
VM_POWERED_OFF = "poweredOff"
VM_POWERED_ON = "poweredOn"

# Azure VM power statuses
VM_STOPPED = "deallocated"
VM_STOPPING = "deallocating"
VM_STARTED = "running"
VM_STARTING = "starting"

# Node statuses
NODE_READY = "Ready"
NODE_NOT_READY = "NotReady"
NODE_READY_SCHEDULING_DISABLED = "Ready,SchedulingDisabled"
NODE_NOT_READY_SCHEDULING_DISABLED = "NotReady,SchedulingDisabled"

# Volume modes
VOLUME_MODE_BLOCK = "Block"
VOLUME_MODE_FILESYSTEM = "Filesystem"

# Alert labels
ALERT_CLUSTERERRORSTATE = "CephClusterErrorState"
ALERT_CLUSTERWARNINGSTATE = "CephClusterWarningState"
ALERT_DATARECOVERYTAKINGTOOLONG = "CephDataRecoveryTakingTooLong"
ALERT_MGRISABSENT = "CephMgrIsAbsent"
ALERT_MONQUORUMATRISK = "CephMonQuorumAtRisk"
ALERT_MONQUORUMLOST = "CephMonQuorumLost"
ALERT_OSDDISKNOTRESPONDING = "CephOSDDiskNotResponding"
ALERT_PGREPAIRTAKINGTOOLONG = "CephPGRepairTakingTooLong"
ALERT_PROMETHEUSRULEFAILURES = "PrometheusRuleFailures"
ALERT_BUCKETREACHINGQUOTASTATE = "NooBaaBucketReachingQuotaState"
ALERT_BUCKETERRORSTATE = "NooBaaBucketErrorState"
ALERT_BUCKETEXCEEDINGQUOTASTATE = "NooBaaBucketExceedingQuotaState"
ALERT_NAMESPACERESOURCEERRORSTATE = "NooBaaNamespaceResourceErrorState"
ALERT_NAMESPACEBUCKETERRORSTATE = "NooBaaNamespaceBucketErrorState"
ALERT_NODEDOWN = "CephNodeDown"
ALERT_CLUSTERNEARFULL = "CephClusterNearFull"
ALERT_CLUSTERCRITICALLYFULL = "CephClusterCriticallyFull"
ALERT_CLUSTEROBJECTSTORESTATE = "ClusterObjectStoreState"
ALERT_KUBEHPAREPLICASMISMATCH = "KubeHpaReplicasMismatch"

# OCS Deployment related constants
OPERATOR_NODE_LABEL = "cluster.ocs.openshift.io/openshift-storage=''"
INFRA_NODE_LABEL = "node-role.kubernetes.io/infra=''"
NODE_SELECTOR_ANNOTATION = "openshift.io/node-selector="
TOPOLOGY_ROOK_LABEL = "topology.rook.io/rack"
OPERATOR_NODE_TAINT = "node.ocs.openshift.io/storage=true:NoSchedule"
OPERATOR_CATALOG_SOURCE_NAME = "redhat-operators"
OSBS_BOUNDLE_IMAGE = "registry-proxy.engineering.redhat.com/rh-osbs/iib-pub-pending"
MARKETPLACE_NAMESPACE = "openshift-marketplace"
MONITORING_NAMESPACE = "openshift-monitoring"
OPERATOR_INTERNAL_SELECTOR = "ocs-operator-internal=true"
OPERATOR_CS_QUAY_API_QUERY = (
    "https://quay.io/api/v1/repository/rhceph-dev/{image}/"
    "tag/?onlyActiveTags=true&limit={tag_limit}&page={page}"
)
OPTIONAL_OPERATORS_SELECTOR = "catalog=optional-operators"
OCS_OPERATOR_BUNDLE_IMAGE = "quay.io/rhceph-dev/ocs-operator-bundle"

# OCP related constants
OPENSHIFT_UPGRADE_INFO_API = (
    "https://api.openshift.com/api/upgrades_info/v1/graph?channel={channel}"
)

# Platforms
AWS_PLATFORM = "aws"
AZURE_PLATFORM = "azure"
GCP_PLATFORM = "gcp"
VSPHERE_PLATFORM = "vsphere"
BAREMETAL_PLATFORM = "baremetal"
IBM_POWER_PLATFORM = "powervs"
BAREMETALPSI_PLATFORM = "baremetalpsi"
RGW_PLATFORM = "rgw"
IBMCLOUD_PLATFORM = "ibm_cloud"
IBM_COS_PLATFORM = "ibmcos"
IBM_PLATFORM = "ibm"
OPENSHIFT_DEDICATED_PLATFORM = "openshiftdedicated"
RHV_PLATFORM = "rhv"
ROSA_PLATFORM = "rosa"
ACM_OCP_DEPLOYMENT = "acm_ocp_deployment"
ON_PREM_PLATFORMS = [
    VSPHERE_PLATFORM,
    BAREMETAL_PLATFORM,
    BAREMETALPSI_PLATFORM,
    IBM_POWER_PLATFORM,
    RHV_PLATFORM,
]
CLOUD_PLATFORMS = [
    AWS_PLATFORM,
    AZURE_PLATFORM,
    GCP_PLATFORM,
    IBM_PLATFORM,
    IBMCLOUD_PLATFORM,
    ROSA_PLATFORM,
    OPENSHIFT_DEDICATED_PLATFORM,
]
MANAGED_SERVICE_PLATFORMS = [
    OPENSHIFT_DEDICATED_PLATFORM,
    ROSA_PLATFORM,
]
BAREMETAL_PLATFORMS = [BAREMETAL_PLATFORM, BAREMETALPSI_PLATFORM]

# AWS i3 worker instance for LSO
AWS_LSO_WORKER_INSTANCE = "i3en.2xlarge"

# ignition files
BOOTSTRAP_IGN = "bootstrap.ign"
MASTER_IGN = "master.ign"
WORKER_IGN = "worker.ign"
SNO_BOOTSTRAP_IGN = "bootstrap-in-place-for-live-iso.ign"

# terraform provider constants
TERRAFORM_IGNITION_PROVIDER_VERSION = "v2.1.0"

# Minimum storage needed for vSphere Datastore in bytes.
MIN_STORAGE_FOR_DATASTORE = 1.1 * 1024**4

# vSphere related constants
VSPHERE_NODE_USER = "core"
VSPHERE_INSTALLER_BRANCH = "release-4.3"
VSPHERE_INSTALLER_REPO = "https://github.com/openshift/installer.git"
VSPHERE_SCALEUP_REPO = "https://code.engineering.redhat.com/gerrit/openshift-misc"
VSPHERE_CLUSTER_LAUNCHER = "https://gitlab.cee.redhat.com/aosqe/v4-scaleup.git"
VSPHERE_DIR = os.path.join(EXTERNAL_DIR, "installer/upi/vsphere/")
INSTALLER_IGNITION = os.path.join(VSPHERE_DIR, "machine/ignition.tf")
VM_IFCFG = os.path.join(VSPHERE_DIR, "vm/ifcfg.tmpl")
INSTALLER_ROUTE53 = os.path.join(VSPHERE_DIR, "route53/main.tf")
INSTALLER_MACHINE_CONF = os.path.join(VSPHERE_DIR, "machine/main.tf")
VM_MAIN = os.path.join(VSPHERE_DIR, "vm/main.tf")
VSPHERE_CONFIG_PATH = os.path.join(TOP_DIR, "conf/ocsci/vsphere_upi_vars.yaml")
VSPHERE_MAIN = os.path.join(VSPHERE_DIR, "main.tf")
VSPHERE_VAR = os.path.join(VSPHERE_DIR, "variables.tf")
VM_VAR = os.path.join(VSPHERE_DIR, "vm/variables.tf")
TERRAFORM_DATA_DIR = "terraform_data"
TERRAFORM_PLUGINS_DIR = ".terraform"
SCALEUP_TERRAFORM_DATA_DIR = "scaleup_terraform_data"
SCALEUP_VSPHERE_DIR = os.path.join(
    EXTERNAL_DIR, "openshift-misc/v4-testing-misc/v4-scaleup/vsphere/"
)
SCALEUP_VSPHERE_MAIN = os.path.join(SCALEUP_VSPHERE_DIR, "main.tf")
SCALEUP_VSPHERE_VARIABLES = os.path.join(SCALEUP_VSPHERE_DIR, "variables.tf")
SCALEUP_VSPHERE_ROUTE53 = os.path.join(
    SCALEUP_VSPHERE_DIR, "route53/vsphere-rhel-dns.tf"
)
SCALEUP_VSPHERE_ROUTE53_VARIABLES = os.path.join(
    SCALEUP_VSPHERE_DIR, "route53/variables.tf"
)
SCALEUP_VSPHERE_MACHINE_CONF = os.path.join(
    SCALEUP_VSPHERE_DIR, "machines/vsphere-rhel-machine.tf"
)
RUST_URL = "https://sh.rustup.rs"
COREOS_INSTALLER_REPO = "https://github.com/coreos/coreos-installer.git"

# v4-scaleup
CLUSTER_LAUNCHER_VSPHERE_DIR = os.path.join(
    EXTERNAL_DIR, "v4-scaleup/ocp4-rhel-scaleup/"
)
CLUSTER_LAUNCHER_MACHINE_CONF = "vsphere/machines/vsphere-rhel-machine.tf"

TERRAFORM_VARS = "terraform.tfvars"
VM_DISK_TYPE = "thin"
VM_DISK_MODE = "persistent"
INSTALLER_DEFAULT_DNS = "1.1.1.1"

LIFECYCLE = 'lifecycle { ignore_changes = ["disk"] }'
CSR_BOOTSTRAPPER_NODE = "node-bootstrapper"

# VMware Datastore types
VMFS = "VMFS"
VSAN = "vsan"

# terraform haproxy service
TERRAFORM_HAPROXY_SERVICE = os.path.join(VSPHERE_DIR, "lb/haproxy.service")

# vSphere IPI related constants
NUM_OF_VIPS = 2

# Config related constants
config_keys_patterns_to_censor = ["passw", "token", "secret", "key", "credential"]

# packages
RHEL_POD_PACKAGES = [
    "openssh-clients",
    "openshift-ansible",
    "openshift-clients",
    "jq",
    "yum-utils",
]

# common locations
POD_UPLOADPATH = RHEL_TMP_PATH = "/tmp/"
YUM_REPOS_PATH = "/etc/yum.repos.d/"
YUM_VARS_PATH = "/etc/yum/vars/"
PEM_PATH = "/etc/pki/ca-trust/source/anchors/"
FIPS_LOCATION = "/proc/sys/crypto/fips_enabled"

# Upgrade related constants, keeping some space between, so we can add
# additional order.
ORDER_BEFORE_UPGRADE = 10
ORDER_BEFORE_OCP_UPGRADE = 20
ORDER_OCP_UPGRADE = 30
ORDER_AFTER_OCP_UPGRADE = 40
ORDER_BEFORE_OCS_UPGRADE = 50
ORDER_OCS_UPGRADE = 60
ORDER_AFTER_OCS_UPGRADE = 70
ORDER_AFTER_UPGRADE = 80

# Deployment constants
OCS_CSV_PREFIX = "ocs-operator"
LOCAL_STORAGE_CSV_PREFIX = "local-storage-operator"
COUCHBASE_CSV_PREFIX = "couchbase-operator"
LATEST_TAGS = (
    "latest",
    "latest-stable",
    "-rc",
)
EC2_USER = "ec2-user"
OCS_SUBSCRIPTION = "ocs-operator"
ODF_SUBSCRIPTION = "odf-operator"
ROOK_OPERATOR_CONFIGMAP = "rook-ceph-operator-config"
ROOK_CONFIG_OVERRIDE_CONFIGMAP = "rook-config-override"
ROOK_CEPH_MON_ENDPOINTS = "rook-ceph-mon-endpoints"
MIRROR_OPENSHIFT_USER_FILE = "mirror_openshift_user"
MIRROR_OPENSHIFT_PASSWORD_FILE = "mirror_openshift_password"
NOOBAA_POSTGRES_CONFIGMAP = "noobaa-postgres-config"
ROOK_CEPH_OPERATOR = "rook-ceph-operator"

# UI Deployment constants
HTPASSWD_SECRET_NAME = "htpass-secret"
HTPASSWD_SECRET_YAML = "frontend/integration-tests/data/htpasswd-secret.yaml"
HTPASSWD_PATCH_YAML = "frontend/integration-tests/data/patch-htpasswd.yaml"
CHROME_BROWSER = "chrome"
SUPPORTED_BROWSERS = CHROME_BROWSER

# Managed service deployment constants
OSD_DEPLOYER = "ocs-osd-deployer"
OSE_PROMETHEUS_OPERATOR = "ose-prometheus-operator"

# Inventory
INVENTORY_TEMPLATE = "inventory.yaml.j2"
INVENTORY_FILE = "inventory.yaml"

INVENTORY_TEMPLATE_HAPROXY = "inventory_haproxy.yaml.j2"
INVENTORY_FILE_HAPROXY = "inventory_haproxy.yaml"

# users
VM_RHEL_USER = "test"

# playbooks
SCALEUP_ANSIBLE_PLAYBOOK = "/usr/share/ansible/openshift-ansible/playbooks/scaleup.yml"

# annotations
REVISION_ANNOTATION = "deployment.kubernetes.io/revision"

# labels
MASTER_LABEL = "node-role.kubernetes.io/master"
WORKER_LABEL = "node-role.kubernetes.io/worker"
APP_LABEL = "node-role.kubernetes.io/app"

# well known topologies
ZONE_LABEL = "topology.kubernetes.io/zone"
REGION_LABEL = "topology.kubernetes.io/region"

# Cluster name limits
CLUSTER_NAME_MIN_CHARACTERS = 5
CLUSTER_NAME_MAX_CHARACTERS = 17

STAGE_CA_FILE = os.path.join(TEMPLATE_DIR, "ocp-deployment", "stage-ca.crt")

# PDB NAMES
MDS_PDB = "rook-ceph-mds-ocs-storagecluster-cephfilesystem"
OSD_PDB = "rook-ceph-osd-"
MON_PDB = "rook-ceph-mon-pdb"

# Root Disk size
CURRENT_VM_ROOT_DISK_SIZE = "60"
VM_ROOT_DISK_SIZE = "120"

# Secrets
RBD_PROVISIONER_SECRET = "rook-csi-rbd-provisioner"
RBD_NODE_SECRET = "rook-csi-rbd-node"
CEPHFS_PROVISIONER_SECRET = "rook-csi-cephfs-provisioner"
CEPHFS_NODE_SECRET = "rook-csi-cephfs-node"
# OSU = ObjectStoreUser, shortened for compliance with flake8+black because of line length issues
OSU_SECRET_BASE = "rook-ceph-object-user-ocs-{}storagecluster-cephobjectstore-{}-{}"
CEPH_OBJECTSTOREUSER_SECRET = OSU_SECRET_BASE.format(
    "", "ocs-storagecluster", "cephobjectstoreuser"
)
CEPH_EXTERNAL_OBJECTSTOREUSER_SECRET = OSU_SECRET_BASE.format(
    "external-", "ocs-storagecluster", "cephobjectstoreuser"
)
NOOBAA_OBJECTSTOREUSER_SECRET = OSU_SECRET_BASE.format(
    "", "noobaa", "ceph-objectstore-user"
)
EXTERNAL_MODE_NOOBAA_OBJECTSTOREUSER_SECRET = OSU_SECRET_BASE.format(
    "external-", "noobaa", "ceph-objectstore-user"
)
OCS_SECRET = "ocs-secret"
AZURE_NOOBAA_SECRET = "noobaa-azure-container-creds"
# Names of Managed Service secrets are derived from addon name
# Following secret strings contain only suffix
MANAGED_SMTP_SECRET_SUFFIX = "-smtp"
MANAGED_PAGERDUTY_SECRET_SUFFIX = "-pagerduty"
MANAGED_DEADMANSSNITCH_SECRET_SUFFIX = "-deadmanssnitch"
MANAGED_PARAMETERS_SECRET_PREFIX = "addon-"
MANAGED_PARAMETERS_SECRET_SUFFIX = "-parameters"
MANAGED_ALERTMANAGER_SECRET = "alertmanager-managed-ocs-alertmanager-generated"
MANAGED_ONBOARDING_SECRET = "onboarding-ticket-key"
MANAGED_PROVIDER_SERVER_SECRET = "ocs-provider-server"
MANAGED_MON_SECRET = "rook-ceph-mon"

# JSON Schema
OSD_TREE_ROOT = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"const": "default"},
        "type": {"const": "root"},
        "type_id": {"const": 11},
        "children": {"type": "array", "items": {"type": "integer"}},
    },
    "required": ["children", "id", "name", "type", "type_id"],
    "additionalProperties": False,
}

OSD_TREE_RACK = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "type": {"const": "rack"},
        "type_id": {"const": 3},
        "pool_weights": {"type": "object"},
        "children": {"type": "array", "items": {"type": "integer"}},
    },
    "required": ["children", "id", "name", "pool_weights", "type", "type_id"],
    "additionalProperties": False,
}

OSD_TREE_HOST = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "type": {"const": "host"},
        "type_id": {"const": 1},
        "pool_weights": {"type": "object"},
        "children": {"type": "array", "items": {"type": "integer"}},
    },
    "required": ["children", "id", "name", "pool_weights", "type", "type_id"],
    "additionalProperties": False,
}

OSD_TREE_OSD = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "device_class": {"type": "string"},
        "name": {"pattern": "osd[.][0-9]+"},
        "type": {"const": "osd"},
        "type_id": {"const": 0},
        "crush_weight": {"type": "number"},
        "depth": {"type": "integer"},
        "pool_weights": {"type": "object"},
        "exists": {"type": "integer"},
        "status": {"const": "up"},
        "reweight": {"type": "integer"},
        "primary_affinity": {"type": "integer"},
    },
    "required": [
        "crush_weight",
        "depth",
        "device_class",
        "exists",
        "id",
        "name",
        "pool_weights",
        "primary_affinity",
        "reweight",
        "status",
        "type",
        "type_id",
    ],
    "additionalProperties": False,
}

OSD_TREE_REGION = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "type": {"const": "region"},
        "type_id": {"const": 10},
        "pool_weights": {"type": "object"},
        "children": {"type": "array", "items": {"type": "integer"}},
    },
    "required": ["children", "id", "name", "pool_weights", "type", "type_id"],
    "additionalProperties": False,
}

OSD_TREE_ZONE = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "type": {"const": "zone"},
        "type_id": {"const": 9},
        "pool_weights": {"type": "object"},
        "children": {"type": "array", "items": {"type": "integer"}},
    },
    "required": ["children", "id", "name", "pool_weights", "type", "type_id"],
    "additionalProperties": False,
}

# gather bootstrap
GATHER_BOOTSTRAP_PATTERN = "openshift-install gather bootstrap --help"

# must-gather commands output files
MUST_GATHER_COMMANDS = [
    "ceph_versions",
    "ceph_status",
    "ceph_report",
    "ceph_pg_dump",
    "ceph_osd_tree",
    "ceph_osd_stat",
    "ceph_osd_dump",
    "ceph_osd_df_tree",
    "ceph_osd_crush_show-tunables",
    "ceph_osd_crush_dump",
    "ceph_mon_stat",
    "ceph_mon_dump",
    "ceph_mgr_dump",
    "ceph_mds_stat",
    "ceph_health_detail",
    "ceph_fs_ls",
    "ceph_fs_dump",
    "ceph_df",
    "ceph_auth_list",
]

MUST_GATHER_COMMANDS_JSON = [
    "ceph_versions_--format_json-pretty",
    "ceph_status_--format_json-pretty",
    "ceph_report_--format_json-pretty",
    "ceph_pg_dump_--format_json-pretty",
    "ceph_osd_tree_--format_json-pretty",
    "ceph_osd_stat_--format_json-pretty",
    "ceph_osd_dump_--format_json-pretty",
    "ceph_osd_df_tree_--format_json-pretty",
    "ceph_osd_crush_show-tunables_--format_json-pretty",
    "ceph_osd_crush_dump_--format_json-pretty",
    "ceph_mon_stat_--format_json-pretty",
    "ceph_mon_dump_--format_json-pretty",
    "ceph_mgr_dump_--format_json-pretty",
    "ceph_mds_stat_--format_json-pretty",
    "ceph_health_detail_--format_json-pretty",
    "ceph_fs_ls_--format_json-pretty",
    "ceph_fs_dump_--format_json-pretty",
    "ceph_df_--format_json-pretty",
    "ceph_auth_list_--format_json-pretty",
]

# local storage
LOCAL_STORAGE_OPERATOR = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "local-storage-operator.yaml"
)
LOCAL_VOLUME_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "local-volume.yaml")
LOCAL_STORAGE_OPTIONAL_OPERATORS = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "local-storage-optional-operators.yaml"
)
LOCAL_VOLUME_DISCOVERY_YAML = os.path.join(
    TEMPLATE_DEPLOYMENT_DIR, "local-volume-discovery.yaml"
)
LOCAL_VOLUME_DISCOVERY = (
    "localvolumediscovery.local.storage.openshift.io/auto-discover-devices"
)
LOCAL_VOLUME_SET_YAML = os.path.join(TEMPLATE_DEPLOYMENT_DIR, "local-volume-set.yaml")
LOCAL_VOLUME_SET = "localvolumesets.local.storage.openshift.io"

AUTO_DISCOVER_DEVICES_RESOURCE = "auto-discover-devices"
LOCAL_BLOCK_RESOURCE = "localblock"

# All worker default config files
RHCOS_WORKER_CONF = os.path.join(CONF_DIR, "ocsci/aws_upi_rhcos_workers.yaml")
AWS_WORKER_NODE_TEMPLATE = "06_cluster_worker_node.yaml"
AWS_S3_UPI_BUCKET = "ocs-qe-upi"
AWS_WORKER_LOGICAL_RESOURCE_ID = "Worker0"
RHEL_WORKERS_CONF = os.path.join(CONF_DIR, "ocsci/aws_upi_rhel{version}_workers.yaml")

# Users
NB_SERVICE_ACCOUNT_BASE = "system:serviceaccount:openshift-storage:{}"
NOOBAA_SERVICE_ACCOUNT_NAME = "noobaa"
NOOBAA_DB_SERVICE_ACCOUNT_NAME = "noobaa-endpoint"
NOOBAA_SERVICE_ACCOUNT = NB_SERVICE_ACCOUNT_BASE.format(NOOBAA_SERVICE_ACCOUNT_NAME)
NOOBAA_DB_SERVICE_ACCOUNT = NB_SERVICE_ACCOUNT_BASE.format(
    NOOBAA_DB_SERVICE_ACCOUNT_NAME
)


# Services
RGW_SERVICE_INTERNAL_MODE = "rook-ceph-rgw-ocs-storagecluster-cephobjectstore"
RGW_SERVICE_EXTERNAL_MODE = "rook-ceph-rgw-ocs-external-storagecluster-cephobjectstore"

# Routes
RGW_ROUTE_INTERNAL_MODE = "ocs-storagecluster-cephobjectstore"
RGW_ROUTE_EXTERNAL_MODE = "ocs-external-storagecluster-cephobjectstore"

# Miscellaneous
NOOBAA_OPERATOR_POD_CLI_PATH = "/usr/local/bin/noobaa-operator"
NOOBAA_OPERATOR_LOCAL_CLI_PATH = os.path.join(DATA_DIR, "mcg-cli")
DEFAULT_INGRESS_CRT = "router-ca.crt"
DEFAULT_INGRESS_CRT_LOCAL_PATH = f"{DATA_DIR}/mcg-{DEFAULT_INGRESS_CRT}"
SERVICE_CA_CRT = "service-ca.crt"
SERVICE_MONITORS = "servicemonitors"
SERVICE_CA_CRT_AWSCLI_PATH = f"/cert/{SERVICE_CA_CRT}"
AWSCLI_RELAY_POD_NAME = "awscli-relay-pod"
AWSCLI_SERVICE_CA_CONFIGMAP_NAME = "awscli-service-ca"
AWSCLI_TEST_OBJ_DIR = "/test_objects/"

# Storage classes provisioners
OCS_PROVISIONERS = [
    "openshift-storage.rbd.csi.ceph.com",
    "openshift-storage.cephfs.csi.ceph.com",
    "openshift-storage.noobaa.io/obc",
    "topolvm.cybozu.com",
]
RBD_PROVISIONER = "openshift-storage.rbd.csi.ceph.com"

# Bucket Policy action lists
bucket_website_action_list = ["PutBucketWebsite", "GetBucketWebsite", "PutObject"]
bucket_version_action_list = ["PutBucketVersioning", "GetBucketVersioning"]
object_version_action_list = ["PutObject", "GetObjectVersion", "DeleteObjectVersion"]

# Flexy config constants
FLEXY_MNT_CONTAINER_DIR = "/mnt"
FLEXY_HOST_DIR = "flexy-dir"
FLEXY_HOST_DIR_PATH = os.path.join(DATA_DIR, FLEXY_HOST_DIR)
FLEXY_DEFAULT_ENV_FILE = "ocs-osp.env"
OPENSHIFT_MISC_BASE = "private-openshift-misc/functionality-testing"
FLEXY_BAREMETAL_UPI_TEMPLATE = "upi-on-baremetal/versioned-installer-openstack"
FLEXY_AWS_UPI_TEMPLATE = "upi-on-aws/versioned-installer"
FLEXY_VSPHERE_UPI_TEMPLATE = "upi-on-aws/versioned-installer"
FLEXY_GIT_CRYPT_KEYFILE = os.path.join(DATA_DIR, "git-crypt-keyfile")
NTP_CHRONY_CONF = os.path.join(TEMPLATE_DIR, "ocp-deployment", "ntp_chrony.yaml")
FLEXY_DEFAULT_PRIVATE_CONF_REPO = (
    "https://gitlab.cee.redhat.com/ocs/flexy-ocs-private.git"
)
FLEXY_JENKINS_USER = "jenkins"
FLEXY_DEFAULT_PRIVATE_CONF_BRANCH = "master"
OPENSHIFT_CONFIG_NAMESPACE = "openshift-config"
FLEXY_RELATIVE_CLUSTER_DIR = "flexy/workdir/install-dir"
FLEXY_IMAGE_URL = "docker-registry.upshift.redhat.com/flexy/ocp4:latest"
FLEXY_ENV_FILE_UPDATED_NAME = "ocs-flexy-env-file-updated.env"
FLEXY_ENV_FILE_UPDATED_PATH = os.path.join(
    FLEXY_HOST_DIR_PATH, FLEXY_ENV_FILE_UPDATED_NAME
)
REGISTRY_SVC = "registry.ci.openshift.org/ocp/release"
FLEXY_USER_LOCAL_UID = 101000

# domains required to be accessible through proxy on disconnected cluster
DISCON_CL_PROXY_ALLOWED_DOMAINS = (
    ".debian.org",
    ".fedoraproject.org",
    "ocsci-test-files.s3.amazonaws.com",
    ".elb.amazonaws.com",
    "s3.openshift-storage.svc",
    ".s3.us-west-1.amazonaws.com",
    ".s3.us-east-2.amazonaws.com",
    "s3.amazonaws.com",
    "mirrorlist.centos.org",
    "mirror.centos.org",
)
# mirrored redhat-operators index image for catalog source namespace and name
MIRRORED_INDEX_IMAGE_NAMESPACE = "olm-mirror"
MIRRORED_INDEX_IMAGE_NAME = "redhat-operator-index"
# following packages are required for live disconnected cluster installation
# (all images related to those packages will be mirrored to the mirror registry)
DISCON_CL_REQUIRED_PACKAGES = [
    "cluster-logging",
    "elasticsearch-operator",
    "local-storage-operator",
    "mcg-operator",
    "noobaa-operator",
    "ocs-operator",
    "odf-csi-addons-operator",
    "odf-lvm-operator",
    "odf-multicluster-orchestrator",
    "odf-operator",
]

DISCON_CL_REQUIRED_PACKAGES_PER_ODF_VERSION = {
    "4.11": [
        "cluster-logging",
        "elasticsearch-operator",
        "mcg-operator",
        "ocs-operator",
        "odf-csi-addons-operator",
        "odf-lvm-operator",
        "odf-multicluster-orchestrator",
        "odf-operator",
    ]
}


# PSI-openstack constants
NOVA_CLNT_VERSION = "2.0"
CINDER_CLNT_VERSION = "3.0"

# URLs
AUTH_CONFIG_DOCS = (
    "https://ocs-ci.readthedocs.io/en/latest/docs/getting_started.html"
    "#authentication-config"
)

# Conversions
TP_CONVERSION = {" B/s": 0.000000976562, " KiB/s": 0.000976562, " MiB/s": 1}

# LSO
ROOT_DISK_NAME = "sda"
RDM = "RDM"
VMDK = "VMDK"
DIRECTPATH = "VMDirectPath"
AWS_EBS = "EBS"
DISK_MODE = "independent_persistent"
COMPATABILITY_MODE = "physicalMode"
DISK_PATH_PREFIX = "/vmfs/devices/disks/"

# OS
RHEL_OS = "RHEL"
RHCOS = "RHCOS"

# Scale constants
SCALE_NODE_SELECTOR = {"scale-label": "app-scale"}
SCALE_LABEL = "scale-label=app-scale"
# TODO: Revisit the dict value once there is change in instance/vm/server type
# TODO: Generic worker count value to support all kind of pods.
# Note: Below worker count value is based on performance pod and each pod
# will be attached with 20 PVC's each, i.e. if we create 3000 PVCs then
# will be creating 150 pods each pod attached with 20 PVCs and in PVC
# there will be minimal fio started
# aws dict value is based on the manual execution result with m5.4xlarge instance and perf pod
# vmware dict value is based on each worker vm config of min 12CPU and 64G RAM
# bm dict value is based on each worker BM machine of config 40CPU and 256G/184G RAM
# azure dict value is based on assumption similar to vmware vms min worker config of 12CPU and 64G RAM
SCALE_WORKER_DICT = {
    40: {"aws": 3, "vmware": 3, "bm": 2, "azure": 3, "rhv": 3},
    80: {"aws": 3, "vmware": 3, "bm": 2, "azure": 3, "rhv": 3},
    240: {"aws": 3, "vmware": 3, "bm": 2, "azure": 3, "rhv": 3},
    1500: {"aws": 3, "vmware": 3, "bm": 2, "azure": 3, "rhv": 3},
    3000: {"aws": 3, "vmware": 3, "bm": 2, "azure": 3, "rhv": 3},
    4500: {"aws": 3, "vmware": 3, "bm": 2, "azure": 3, "rhv": 3},
    6000: {"aws": 6, "vmware": 6, "bm": 4, "azure": 6, "rhv": 6},
    9000: {"aws": 6, "vmware": 6, "bm": 4, "azure": 6, "rhv": 6},
}
SCALE_MAX_PVCS_PER_NODE = 500
SCALE_PVC_ROUND_UP_VALUE = {
    40: 40,
    80: 80,
    240: 240,
    1500: 1520,
    3000: 3040,
    4500: 4560,
    6000: 6080,
    9000: 9120,
}

# Production config instance type
AWS_PRODUCTION_INSTANCE_TYPE = "m5.4xlarge"
AZURE_PRODUCTION_INSTANCE_TYPE = "Standard_D16s_v3"

# Cluster metrics
THROUGHPUT_QUERY = "(sum(rate(ceph_pool_wr_bytes[1m]) + rate(ceph_pool_rd_bytes[1m])))"
LATENCY_QUERY = "cluster:ceph_disk_latency:join_ceph_node_disk_irate1m"
IOPS_QUERY = "sum(rate(ceph_pool_wr[1m])) + sum(rate(ceph_pool_rd[1m]))"
USED_SPACE_QUERY = "ceph_cluster_total_used_bytes"

# files
REMOTE_FILE_URL = "http://download.ceph.com/tarballs/ceph_15.1.0.orig.tar.gz"
FILE_PATH = "/tmp/ceph.tar.gz"

# terraform tfstate modules
BOOTSTRAP_MODULE = "module.ipam_bootstrap"
LOAD_BALANCER_MODULE = "module.ipam_lb"
COMPUTE_MODULE = "module.ipam_compute"
CONTROL_PLANE = "module.ipam_control_plane"
COMPUTE_MODULE_VM = "module.compute_vm"

# proxy location
HAPROXY_LOCATION = "/etc/haproxy/haproxy.cfg"
HAPROXY_SERVICE = "/etc/systemd/system/haproxy.service"

# chrony conf
CHRONY_CONF = "/etc/chrony.conf"

# NTP server
RH_NTP_CLOCK = "clock1.rdu2.redhat.com"

# Disruptions pod names
OSD = "osd"
ROOK_OPERATOR = "operator"
MON_DAEMON = "mon"

# cluster expansion
MAX_OSDS = 18

# Minimum cluster requirements in term of node specs
MIN_NODE_CPU = 16
MIN_NODE_MEMORY = 64 * 10**9

# aws tags
AWS_CLOUDFORMATION_TAG = "aws:cloudformation:stack-name"

# Bare Metal constants
PXE_CONF_FILE = os.path.join(TEMPLATE_DIR, "ocp-deployment", "dnsmasq.pxe.conf")
COMMON_CONF_FILE = os.path.join(TEMPLATE_DIR, "ocp-deployment", "dnsmasq.common.conf")
RHCOS_IMAGES_FILE = os.path.join(TEMPLATE_DIR, "ocp-deployment", "rhcos_images.yaml")
PXE_FILE = os.path.join(TEMPLATE_DIR, "baremetal-pxefile")
coreos_url_prefix = "https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos"
BM_DEFAULT_CLUSTER_NAME = "ocp-baremetal-auto"
BM_STATUS_ABSENT = "ABSENT"
BM_STATUS_PRESENT = "PRESENT"
BM_STATUS_RESPONSE_UPDATED = "UPDATED"
BM_METAL_IMAGE = "rhcos-metal.x86_64.raw.gz"

# RHV related constants
RHV_CONFIG_FILEPATH = os.path.expanduser("~/.ovirt/ovirt-config.yaml")
RHV_DISK_FORMAT_COW = "COW"
RHV_DISK_FORMAT_RAW = "RAW"
RHV_DISK_INTERFACE_VIRTIO_SCSI = "VIRTIO_SCSI"

# MCG constants
PLACEMENT_BUCKETCLASS = "placement-bucketclass"
AWS_S3_ENDPOINT = "https://s3.amazonaws.com"
NAMESPACE_FILESYSTEM = "nsfs"

# Cosbench constants
COSBENCH = "cosbench"
COSBENCH_PROJECT = "cosbench-project"
COSBENCH_IMAGE = "quay.io/ocsci/cosbench:latest"
COSBENCH_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "cosbench")
COSBENCH_POD = os.path.join(COSBENCH_DIR, "cosbench_pod.yaml")
COSBENCH_CONFIGMAP = os.path.join(COSBENCH_DIR, "cosbench_configmap.yaml")

# Quay operator constants
QUAY_OPERATOR = "quay-operator"
OPENSHIFT_OPERATORS = "openshift-operators"
QUAY_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "quay")
QUAY_SUB = os.path.join(QUAY_DIR, "quay_subscription.yaml")
QUAY_SUPER_USER = os.path.join(QUAY_DIR, "quay_super_user_config.yaml")
QUAY_REGISTRY = os.path.join(QUAY_DIR, "quay_registry.yaml")

# Quay operator registry API
QUAY_SUPERUSER = "quayadmin"
QUAY_PW = "quaypass123"
QUAY_USER_INIT = "api/v1/user/initialize"
QUAY_USER_GET = "api/v1/superuser/users/"
QUAY_ORG_POST = "api/v1/organization/"
QUAY_REPO_POST = "api/v1/repository"

# logreader workload deployment yaml files
LOGWRITER_DIR = os.path.join(TEMPLATE_WORKLOAD_DIR, "logwriter")
LOGWRITER_CEPHFS_REPRODUCER = os.path.join(LOGWRITER_DIR, "cephfs.reproducer.yaml")
LOGWRITER_CEPHFS_READER = os.path.join(LOGWRITER_DIR, "cephfs.logreader.yaml")
LOGWRITER_CEPHFS_WRITER = os.path.join(LOGWRITER_DIR, "cephfs.logwriter.yaml")

# MCG namespace constants
MCG_NS_AWS_ENDPOINT = "https://s3.amazonaws.com"
MCG_NS_AZURE_ENDPOINT = "https://blob.core.windows.net"
MCG_NS_RESOURCE = "ns_resource"
MCG_NSS = "ns-store"
MCG_NS_BUCKET = "ns-bucket"
MCG_CONNECTION = "connection"
NAMESPACE_POLICY_TYPE_SINGLE = "Single"
NAMESPACE_POLICY_TYPE_MULTI = "Multi"
NAMESPACE_POLICY_TYPE_CACHE = "Cache"

# MCG version-dependent constants
OBJECTBUCKETNAME_46ANDBELOW = "ObjectBucketName"
OBJECTBUCKETNAME_47ANDABOVE = "objectBucketName"

# Cloud provider default endpoints
# Upon use, utilize .format() to replace the curly braces where necessary
AZURE_BLOB_ENDPOINT_TEMPLATE = "https://{}.blob.core.windows.net"
IBM_COS_GEO_ENDPOINT_TEMPLATE = "https://s3.{}.cloud-object-storage.appdomain.cloud"

# NooBaa backingstore types
BACKINGSTORE_TYPE_AWS = "aws-s3"
BACKINGSTORE_TYPE_AZURE = "azure-blob"
BACKINGSTORE_TYPE_S3_COMP = "s3-compatible"
BACKINGSTORE_TYPE_GOOGLE = "google-cloud-storage"

# Squads assignment
# Tests are assigned to Squads based on patterns matching test path.
# For example: In case following test fails:
# tests/e2e/registry/test_pod_from_registry.py::TestRegistryImage::test_run_pod_local_image
# the pattern "/registry/" match the test path and so the test belongs to
# Magenta squad.
SQUADS = {
    "Brown": ["/z_cluster/"],
    "Green": ["/pv_services/", "/storageclass/"],
    "Blue": ["/monitoring/"],
    "Red": ["/mcg/", "/rgw/"],
    "Purple": ["/ecosystem/"],
    "Magenta": ["/workloads/", "/flowtest/", "/lifecycle/", "/kcs/", "/system_test/"],
    "Grey": ["/performance/"],
    "Orange": ["/scale/"],
    "Black": ["/ui/"],
    "Yellow": ["/managed-service/"],
}

PRODUCTION_JOBS_PREFIX = ["jnk"]

# Cloud Manager available platforms
CLOUD_MNGR_PLATFORMS = ["AWS", "GCP", "AZURE", "IBMCOS"]

# Vault related configurations
VAULT_VERSION_INFO_URL = "https://github.com/hashicorp/vault/releases/latest"
VAULT_DOWNLOAD_BASE_URL = "https://releases.hashicorp.com/vault"

# Vault related constants
VAULT_DEFAULT_NAMESPACE = ""
VAULT_DEFAULT_PATH_PREFIX = "ocs"
VAULT_DEFAULT_POLICY_PREFIX = "rook"
VAULT_DEFAULT_NAMESPACE_PREFIX = "ocs-namespace"
VAULT_DEFAULT_TLS_SERVER = ""
VAULT_KMS_CONNECTION_DETAILS_RESOURCE = "ocs-kms-connection-details"
VAULT_KMS_TOKEN_RESOURCE = "ocs-kms-token"
VAULT_CLIENT_CERT_PATH = os.path.join(DATA_DIR, "vault-client.crt")
VAULT_KMS_PROVIDER = "vault"
HPCS_KMS_PROVIDER = "hpcs"
VAULT_NOOBAA_ROOT_SECRET_PATH = "NOOBAA_ROOT_SECRET_PATH"
VAULT_KMS_CSI_CONNECTION_DETAILS = "csi-kms-connection-details"
VAULT_KMS_CSI_TOKEN = "ceph-csi-kms-token"
VAULT_CWD_KMS_SA_NAME = "odf-vault-auth"
VAULT_TOKEN_AUTH = "token"
VAULT_KUBERNETES_AUTH = "kubernetes"
VAULT_KUBERNETES_AUTH_ROLE = "odf-rook-ceph-op"
VAULT_HCP_NAMESPACE = "admin"
# min and max Noobaa endpoints
MIN_NB_ENDPOINT_COUNT_POST_DEPLOYMENT = 1
MCG_TESTS_MIN_NB_ENDPOINT_COUNT = 2
MAX_NB_ENDPOINT_COUNT = 2

VOLUMESNAPSHOT = "volumesnapshot"
LOGICALVOLUME = "logicalvolume"

PERF_IMAGE = "quay.io/ocsci/perf:latest"

ROOK_CEPH_CONFIG_VALUES = """
[global]
mon_osd_full_ratio = .85
mon_osd_backfillfull_ratio = .8
mon_osd_nearfull_ratio = .75
mon_max_pg_per_osd = 600
[osd]
osd_memory_target_cgroup_limit_ratio = 0.5
"""

ROOK_CEPH_CONFIG_VALUES_48 = """
[global]
bdev_flock_retry = 20
mon_osd_full_ratio = .85
mon_osd_backfillfull_ratio = .8
mon_osd_nearfull_ratio = .75
mon_max_pg_per_osd = 600
mon_pg_warn_max_object_skew = 0
[osd]
osd_memory_target_cgroup_limit_ratio = 0.5
"""

ROOK_CEPH_CONFIG_VALUES_49 = """
[global]
bdev_flock_retry = 20
mon_osd_full_ratio = .85
mon_osd_backfillfull_ratio = .8
mon_osd_nearfull_ratio = .75
mon_max_pg_per_osd = 600
mon_pg_warn_max_object_skew = 0
mon_data_avail_warn = 15
[osd]
osd_memory_target_cgroup_limit_ratio = 0.5
"""

ROOK_CEPH_CONFIG_VALUES_410 = """
[global]
bdev_flock_retry = 20
mon_osd_full_ratio = .85
mon_osd_backfillfull_ratio = .8
mon_osd_nearfull_ratio = .75
mon_max_pg_per_osd = 600
mon_pg_warn_max_object_skew = 0
mon_data_avail_warn = 15
[osd]
osd_memory_target_cgroup_limit_ratio = 0.8
"""

CEPH_DEBUG_CONFIG_VALUES = """
[mon]
debug_mon = 20
debug_ms = 1
debug_paxos = 20
debug_crush = 20
"""


# Values from configmap noobaa-postgres-config
NOOBAA_POSTGRES_TUNING_VALUES = """
max_connections = 300
shared_buffers = 1GB
effective_cache_size = 3GB
maintenance_work_mem = 256MB
checkpoint_completion_target = 0.9
wal_buffers = 16MB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 300
work_mem = 1747kB
min_wal_size = 2GB
max_wal_size = 8GB
shared_preload_libraries = 'pg_stat_statements'
"""

# Values from configmap noobaa-postgres-config wrt OCP version 4.10 and above
NOOBAA_POSTGRES_TUNING_VALUES_4_10 = """
max_connections = 600
shared_buffers = 1GB
effective_cache_size = 3GB
maintenance_work_mem = 256MB
checkpoint_completion_target = 0.9
wal_buffers = 16MB
default_statistics_target = 100
random_page_cost = 1.1
effective_io_concurrency = 300
work_mem = 1747kB
min_wal_size = 2GB
max_wal_size = 8GB
shared_preload_libraries = 'pg_stat_statements'
"""

WORKLOAD_STORAGE_TYPE_BLOCK = "block"
WORKLOAD_STORAGE_TYPE_FS = "fs"
# Components of OCS
OCS_COMPONENTS = ["rgw", "cephfs", "noobaa", "blockpools"]
OCS_COMPONENTS_MAP = {
    "rgw": "cephObjectStores",
    "cephfs": "cephFilesystems",
    "noobaa": "multiCloudGateway",
    "blockpools": "cephBlockPools",
}

DEFAULT_PAXOS_SERVICE_TRIM_MIN = 250
DEFAULT_PAXOS_SERVICE_TRIM_MAX = 500
DEFAULT_OSD_OP_COMPLAINT_TIME = 30.000000

# Separators
SHA_SEPARATOR = "@sha256:"

# ibmcloud related constants
IBMCLOUD_VOLUME_NAME = "ibmvolume"

# manifest.json and background.js files used for Chrome extention configuring
# authenticated proxy, see also:
# https://botproxy.net/docs/how-to/setting-chromedriver-proxy-auth-with-selenium-using-python/
CHROME_PROXY_EXTENSION_MANIFEST_TEMPLATE = os.path.join(
    "ui", "chrome-proxy-extension-manifest.json.j2"
)
CHROME_PROXY_EXTENSION_BACKGROUND_TEMPLATE = os.path.join(
    "ui", "chrome-proxy-extension-background.js.j2"
)

# storage system status
STORAGE_SYSTEM_STATUS = {
    "Available": "True",
    "Progressing": "False",
    "StorageSystemInvalid": "False",
    "VendorCsvReady": "True",
    "VendorSystemPresent": "True",
}

PATCH_DEFAULT_SOURCES_CMD = (
    "oc patch operatorhub.config.openshift.io/cluster -p="
    '\'{{"spec":{{"disableAllDefaultSources":{disable}}}}}\' --type=merge'
)
PATCH_SPECIFIC_SOURCES_CMD = (
    "oc patch operatorhub.config.openshift.io/cluster -p="
    '\'{{"spec":{{"sources":[{{"disabled":{disable},"name":"{source_name}"'
    "}}]}}}}' --type=merge"
)

# Submariner constants
SUBMARINER_GATEWAY_NODE_LABEL = "submariner.io/gateway=true"

# Multicluster related

# OpenSSL Certificate parameters
OPENSSL_KEY_SIZE = 2048
OPENSSL_CERT_COUNTRY_NAME = ".."
OPENSSL_CERT_STATE_OR_PROVINCE_NAME = "."
OPENSSL_CERT_LOCALITY_NAME = "."
OPENSSL_CERT_ORGANIZATION_NAME = "OCS"
OPENSSL_CERT_ORGANIZATIONAL_UNIT_NAME = "OCS-QE"
OPENSSL_CERT_EMAIL_ADDRESS = "ocs-qe@redhat.com"

# ACM Hub Parameters
ACM_HUB_OPERATORGROUP_YAML = os.path.join(
    TEMPLATE_DIR, "acm-deployment", "operatorgroup.yaml"
)
ACM_HUB_SUBSCRIPTION_YAML = os.path.join(
    TEMPLATE_DIR, "acm-deployment", "subscription.yaml"
)
ACM_HUB_MULTICLUSTERHUB_YAML = os.path.join(
    TEMPLATE_DIR, "acm-deployment", "multiclusterhub.yaml"
)
ACM_HUB_NAMESPACE = "open-cluster-management"
ACM_HUB_OPERATOR_NAME = "advanced-cluster-management"
ACM_MULTICLUSTER_HUB = "MultiClusterHub"
ACM_MULTICLUSTER_RESOURCE = "multiclusterhub"
ACM_HUB_UNRELEASED_DEPLOY_REPO = "https://github.com/stolostron/deploy.git"
ACM_HUB_UNRELEASED_ICSP_YAML = os.path.join(
    TEMPLATE_DIR, "acm-deployment", "imagecontentsourcepolicy.yaml"
)
ACM_HUB_UNRELEASED_PULL_SECRET_TEMPLATE = "pull-secret.yaml.j2"
ACM_ODF_MULTICLUSTER_ORCHESTRATOR_RESOURCE = "odf-multicluster-orchestrator"
ACM_ODR_HUB_OPERATOR_RESOURCE = "odr-hub-operator"

# Vault encryption KMS types for PV encryption
VAULT_TOKEN = "vaulttokens"
VAULT_TENANT_SA = "vaulttenantsa"
RBD_CSI_VAULT_TOKEN_REVIEWER_NAME = "rbd-csi-vault-token-review"
# ACM UI related constants
PLATFORM_XPATH_MAP = {
    "vsphere": "cc_provider_vmware_vsphere",
    "AWS": None,
    "baremetal": None,
    "azure": None,
}
ACM_PLATOFRM_VSPHERE_CRED_PREFIX = "vsphereacmocp-"
# example release image url : quay.io/openshift-release-dev/ocp-release:4.9.23-x86_64
ACM_OCP_RELEASE_IMG_URL_PREFIX = "registry.ci.openshift.org/ocp/release"
ACM_VSPHERE_NETWORK = "VM Network"
ACM_CLUSTER_DEPLOY_TIMEOUT = 2700  # 45 minutes
ACM_CLUSTER_DESTROY_TIMEOUT = 2700  # 45 minutes
ACM_CLUSTER_DEPLOYMENT_LABEL_KEY = "hive.openshift.io/cluster-deployment-name"
ACM_CLUSTER_DEPLOYMENT_SECRET_TYPE_LABEL_KEY = "hive.openshift.io/secret-type"
# Concatenated CA file for vcenter
VSPHERE_CA_FILE_PATH = os.path.join(DATA_DIR, "vsphere_ca.crt")
SSH_PRIV_KEY = os.path.expanduser(os.path.join(".ssh", "openshift-dev.pem"))
SSH_PUB_KEY = os.path.expanduser(os.path.join(".ssh", "openshift-dev.pub"))
SPACE = " "

# Longevity constants
STAGE_0_NAMESPACE = "ever-running-project"
# Sno and lvmo constants
SNO_NODE_NAME = "sno-edge-0"
LVMO_POD_LABEL = {
    "410": {
        "controller_manager_label": "control-plane=controller-manager",
        "topolvm-controller_label": "app.kubernetes.io/name=topolvm-controller",
        "topolvm-node_label": "app=topolvm-node",
        "vg-manager_label": "app=vg-manager",
    },
    "411": {
        "controller_manager_label": "app.kubernetes.io/name=lvm-operator",
        "topolvm-controller_label": "app.kubernetes.io/name=topolvm-controller",
        "topolvm-node_label": "app.kubernetes.io/name=topolvm-node",
        "vg-manager_label": "app.kubernetes.io/name=vg-manager",
    },
    "411-old": {
        "controller_manager_label": "app.kubernetes.io/name=lvm-operator",
        "topolvm-controller_label": "app.lvm.openshift.io=topolvm-controller",
        "topolvm-node_label": "app.lvm.openshift.io=topolvm-node",
        "vg-manager_label": "app.lvm.openshift.io=vg-manager",
    },
}
LVM_PROVISIONER = "topolvm.cybozu.com"