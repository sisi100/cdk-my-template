import os

from aws_cdk import core

from stacks.api_lambda_integration import ApiLambdaIntegrationStack
from stacks.clear_stack import ClearStack
from stacks.dynamo_table_stack import DynamoTableStack
from stacks.lambda_layer_stack import LambdaLayerStack
from stacks.lambda_trigger_s3_stack import LambdaTriggerS3Stack
from stacks.same_resource import SameResourceStack

app = core.App()
env = core.Environment(account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION"))

# Stacks
ClearStack(app, "clear-stack", env=env)
LambdaLayerStack(app, "lambda-layer-stack", env=env)
DynamoTableStack(app, "dynamo-table-stack", env=env)
ApiLambdaIntegrationStack(app, "api-lambda-integration-stack", env=env)

lambda_trigger_s3_stack = LambdaTriggerS3Stack(app, "lambda-trigger-s3-stack", env=env)
SameResourceStack(app, "same-resources-stack", put_bucket=lambda_trigger_s3_stack.bucket, env=env)

app.synth()
