import aws_cdk.core as core

from my_first_cdk_project.my_first_cdk_project_stack import MyArtifactBucketStack

env_US = core.Environment(region="us-west-2")
env_EUROPE = core.Environment(region="eu-west-2")
app = core.App()
MyArtifactBucketStack(app, "MyDevStack",env=env_US)
MyArtifactBucketStack(app, "MyProdStack",is_prod=True, env=env_US)

app.synth()
