from aws_cdk import aws_apigateway, aws_lambda, core


class ApiLambdaIntegrationStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # lambda
        lambda_ = aws_lambda.Function(
            self,
            "ApiLambdaIntegrationLambda",
            code=aws_lambda.Code.asset("lambdas/api_lambda_integration"),
            runtime=aws_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.lambda_handler",
        )

        # API Gateway
        api = aws_apigateway.RestApi(self, "ApiLambdaIntegrationApiGateway")
        hoge_resources = api.root.add_resource("hoge")
        hoge_resources.add_method(
            "GET",
            aws_apigateway.LambdaIntegration(lambda_),
            request_parameters={
                # URLクエリーパラメータを設定する
                "method.request.querystring.hoge": True,
                "method.request.querystring.hogeOption": False,
            },
            # バリデーターを設定しないとパラメータの必須フラグは動作しない
            request_validator=api.add_request_validator(
                "ApiLambdaIntegrationValidator", validate_request_parameters=True
            ),
        )
