from aws_cdk import aws_lambda, aws_s3, core
from aws_cdk.aws_lambda_event_sources import S3EventSource


class LambdaTriggerS3Stack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # S3
        bucket = aws_s3.Bucket(
            self,
            "LambdaTriggerS3Bucket",
            removal_policy=core.RemovalPolicy.DESTROY,  # Stack削除と同時にバケットを削除する
        )

        # lambda
        common_lambda_params = dict(
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.lambda_handler",
            timeout=core.Duration.seconds(10),
            memory_size=128,
        )
        lambda_ = aws_lambda.Function(
            self,
            "LambdaTriggerS3Lambda",
            code=aws_lambda.Code.asset("lambdas/lambda_trigger_s3"),
            **common_lambda_params,
        )

        # lambdaにtriggerを付与
        lambda_.add_event_source(
            S3EventSource(
                bucket,
                events=[aws_s3.EventType.OBJECT_CREATED_PUT],
                # filterを設定する場合は、下記のコメントアウトを外す
                # filters=[aws_s3.NotificationKeyFilter(prefix="カスタムプレフィックス/", suffix="拡張子")],
            )
        )

        # lambdaの権限
        bucket.grant_read(lambda_)
