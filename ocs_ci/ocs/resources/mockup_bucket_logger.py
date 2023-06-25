from datetime import datetime
import logging
import uuid

from ocs_ci.ocs import constants
from ocs_ci.ocs.bucket_utils import (
    craft_s3_command,
    list_objects_from_bucket,
    sync_object_directory,
)


logger = logging.getLogger(__name__)


class MockupBucketLogger:
    """
    Peforms S3 operations on an MCG bucket and write mathcing mockup logs
    directly to an uls bucket via a Namespacestore MCG bucket.
    """

    def __init__(self, awscli_pod, mcg_obj, bucket_factory, platform, region):
        """
        Args:
            awscli_pod(Pod): A pod running the AWS CLI
            cloud_uls_factory: TODO
        """

        self.awscli_pod = awscli_pod
        self.mcg_obj = mcg_obj

        logger.info("Creating the AWS logs bucket Namespacestore")

        bucketclass_dict = {
            "interface": "OC",
            "namespace_policy_dict": {
                "type": "Single",
                "namespacestore_dict": {platform: [(1, region)]},
            },
        }
        logs_bucket = bucket_factory(bucketclass=bucketclass_dict)[0]
        self.logs_bucket_mcg_name = logs_bucket.name
        self.logs_bucket_uls_name = logs_bucket.bucketclass.namespacestores[0].uls_name

    def upload_test_objs_and_log(self, bucket_name):
        """
        Uploads files from files_dir to the MCG bucket and write matching
        mockup logs to the logs bucket.

        Args:
            files_dir(str): Full path to a directory on awscli_pod
        """
        standard_test_obj_list = self.awscli_pod.exec_cmd_on_pod(
            f"ls -A1 {constants.AWSCLI_TEST_OBJ_DIR}"
        ).split(" ")

        sync_object_directory(
            self.awscli_pod,
            constants.AWSCLI_TEST_OBJ_DIR,
            f"s3://{bucket_name}",
            self.mcg_obj,
        )

        # TODO - use a constant for the ops
        self.__log_ops_for_objects(
            bucket_name=bucket_name, obj_list=standard_test_obj_list, op="PUT"
        )

    def delete_files_and_log(self, bucket_name):
        """
        TODO
        """
        obj_list = list_objects_from_bucket(self.awscli_pod, bucket_name, self.mcg_obj)

        s3cmd = craft_s3_command(f"rm s3://{bucket_name} --recursive", self.mcg_obj)
        self.awscli_pod.exec_cmd_on_pod(s3cmd)

        # TODO: use a constant for the op
        self.__log_ops_for_objects(bucket_name, obj_list, "DELETE")

    def __log_ops_for_objects(self, bucket_name, obj_list, op):
        """
        TODO
        """
        # TODO - make a class scoped const for "/log_files"
        self.awscli_pod.exec_cmd_on_pod("mkdir /log_files")
        for obj_name in obj_list:
            s3mockuplog = S3MockupLog(bucket_name, obj_name, op)
            command = (
                "bash -c "
                + '"echo '
                + f"'{s3mockuplog}'"
                + f'  > /log_files/{s3mockuplog.log_file_name}"'
            )
            self.awscli_pod.exec_cmd_on_pod(command)

        sync_object_directory(
            self.awscli_pod,
            "/log_files",
            f"s3://{self.logs_bucket_mcg_name}",
            self.mcg_obj,
        )

        self.awscli_pod.exec_cmd_on_pod("rm -rf /log_files")


class S3MockupLog:
    """
    TODO
    """

    OP_CODES = {
        "PUT": 200,
        "DELETE": 204,
        "GET": 206,
    }

    def __init__(self, aws_bucket_name, object_key, operation):
        self.aws_bucket_name = aws_bucket_name
        self.object_key = object_key
        self.operation = operation = str.upper(operation)
        self.op_code = S3MockupLog.OP_CODES[operation]
        self._creation_time = datetime.utcnow()
        self._file_name = self._generate_unique_log_file_name()

        with open(constants.AWS_BUCKET_LOG_TEMPLATE, "r") as f:
            self.format = f.read()

        def _generate_unique_log_file_name(self):
            time = self.creation_time.strftime("%Y-%m-%d-%H-%M-%S")
            unique_id = str(uuid.uuid4().hex)[:16].upper()
            return time + unique_id

    @property
    def log_file_name(self):
        return self._file_name

    @property
    def time(self):
        """
        Get the current time as a string in the AWS logs format.
        i.e "[06/Feb/2019:00:00:38 +0000]"
        """
        format_pattern = "[%d/%b/%Y:%H:%M:%S +0000]"
        return self._creation_time.strftime(format_pattern)

    def __str__(self):
        raw_log = self.format.format(
            bucket=self.aws_bucket_name,
            time=self.time,
            object_key=self.object_key,
            op=self.operation,
            op_code=self.op_code,
        )

        # Adjust for python parsing
        adjusted_log = raw_log.replace('"', '\\"')
        return adjusted_log