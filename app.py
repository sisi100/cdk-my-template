import os

from aws_cdk import core

from stacks.clear_stack import ClearStack
from stacks.lambda_trigger_s3_stack import LambdaTriggerS3Stack
from stacks.lambda_layer_stack import LambdaLayerStack

app = core.App()
env = core.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION"))

# Stacks
ClearStack(app, "clear-stack", env=env)
LambdaTriggerS3Stack(app, "lambda-trigger-s3-stack", env=env)
LambdaLayerStack(app, "lambda-layer-stack", env=env)

app.synth()
