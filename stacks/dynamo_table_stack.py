from aws_cdk import core
from aws_cdk.aws_dynamodb import Attribute, AttributeType, BillingMode, Table


class DynamoTableStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # DynamoDB
        table = Table(
            self,
            "DynamoTableTable",
            partition_key=Attribute(name="pk", type=AttributeType.NUMBER),  # パーテーションキー
            sort_key=Attribute(name="sk", type=AttributeType.STRING),  # ソートキー
            billing_mode=BillingMode.PAY_PER_REQUEST,  # オンデマンドに設定
            removal_policy=core.RemovalPolicy.DESTROY,  # Stackの削除と一緒にテーブルを削除する(オプション)
        )
