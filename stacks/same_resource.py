from aws_cdk import aws_lambda, aws_s3, core


class SameResourceStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, put_bucket: aws_s3.Bucket, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # lambda
        lambda_ = aws_lambda.Function(
            self,
            "SameResourceLambda",
            code=aws_lambda.Code.asset("lambdas/same_resource"),
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.lambda_handler",
            environment={"PUT_BUCKET_NAME": put_bucket.bucket_name},
        )

        # lambdaの権限
        put_bucket.grant_write(lambda_)
