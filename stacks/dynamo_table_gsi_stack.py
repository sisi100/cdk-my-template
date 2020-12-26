from aws_cdk import core
from aws_cdk.aws_dynamodb import Attribute, AttributeType, ProjectionType, Table


class DynamoTableGsiStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = Table(
            self,
            "DynamoTableGsiTable",
            partition_key=Attribute(name="pk", type=AttributeType.NUMBER),
            sort_key=Attribute(name="sk", type=AttributeType.STRING),
        )

        table.add_global_secondary_index(
            index_name="HogeGSI",
            partition_key=Attribute(name="gsi_pk", type=AttributeType.NUMBER),
            sort_key=Attribute(name="gsi_sk", type=AttributeType.STRING),
            projection_type=ProjectionType.INCLUDE,
            non_key_attributes=["projection_param_a", "projection_param_b"],  # INCLUDEでプロジェクションするアトリビュート
        )
