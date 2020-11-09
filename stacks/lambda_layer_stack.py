from aws_cdk import aws_lambda, core


class LambdaLayerStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # lambda_layer
        layer = aws_lambda.LayerVersion(
            self,
            "LambdaLayerLayer",
            compatible_runtimes=[aws_lambda.Runtime.PYTHON_3_8],
            code=aws_lambda.AssetCode("layers/lambda_layer"),
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
            "LambdaLayerLambda",
            code=aws_lambda.Code.asset("lambdas/lambda_layer"),
            layers=[layer],
            **common_lambda_params,
        )
