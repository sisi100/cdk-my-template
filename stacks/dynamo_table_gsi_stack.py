from aws_cdk import aws_lambda, core
from aws_cdk.aws_dynamodb import Attribute, AttributeType, ProjectionType, Table


class DynamoTableGsiStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # =======> DynamoDB

        gsi_name = "HogeGSI"

        table = Table(
            self,
            "DynamoTableGsiTable",
            partition_key=Attribute(name="pk", type=AttributeType.NUMBER),
            sort_key=Attribute(name="sk", type=AttributeType.STRING),
            removal_policy=core.RemovalPolicy.DESTROY,
        )

        table.add_global_secondary_index(
            index_name=gsi_name,
            partition_key=Attribute(name="gsi_pk", type=AttributeType.NUMBER),
            sort_key=Attribute(name="gsi_sk", type=AttributeType.STRING),
            projection_type=ProjectionType.KEYS_ONLY,
        )

        # =======> Lambda

        lambda_ = aws_lambda.Function(
            self,
            "LambdaDynamoTableGsi",
            code=aws_lambda.Code.asset("lambdas/dynamo_table_gsi"),
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.lambda_handler",
            environment={"TABLE_NAME": table.table_name, "GSI_NAME": gsi_name},
        )
        table.grant_read_data(lambda_)  # これがあればGSIに読み込み権限が付与される
