import aws_cdk.aws_s3 as _s3
from aws_cdk.core import Stack
from constructs import Construct
import aws_cdk.core as core

class MyArtifactBucketStack(Stack):

    def __init__(self, scope: Construct, construct_id: str,is_prod=False, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        if is_prod:
            artifactBucket = _s3.Bucket(self,
                                        "myProdArtifactBucketId",
                                        versioned=True,
                                        encryption=_s3.BucketEncryption.S3_MANAGED,
                                        removal_policy=core.RemovalPolicy.RETAIN)
        else:
            artifactBucket=_s3.Bucket(self,
                                        "myDevArtifactBucketId")
