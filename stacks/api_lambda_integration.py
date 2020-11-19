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
        api = aws_apigateway.RestApi(
            self, "ApiLambdaIntegrationApiGateway", deploy_options=aws_apigateway.StageOptions(stage_name="hogehoge")
        )
        hoge_resources = api.root.add_resource("hoge")
        hoge_resources.add_method(
            "GET",
            aws_apigateway.LambdaIntegration(lambda_),
            request_parameters={
                # クエリ文字列（URLパラメータ）の明示的に宣言
                "method.request.querystring.hoge": True,  # 必須
                "method.request.querystring.hogeOption": False,  # 必須ではない
            },
            # 下記設定を入れないと必須フラグは動作しない
            request_validator=api.add_request_validator(
                "ApiLambdaIntegrationValidator", validate_request_parameters=True
            ),
        )
