import os

from aws_cdk import core

from stacks.clear_stack import ClearStack

app = core.App()
env = core.Environment(
    account=os.getenv("CDK_DEFAULT_ACCOUNT"), region=os.getenv("CDK_DEFAULT_REGION")
)
ClearStack(app, "clear-stack", env=env)

app.synth()
