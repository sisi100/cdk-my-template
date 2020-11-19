def lambda_handler(event, context):
    query = event["queryStringParameters"]

    return {
        "statusCode": 200,
        "body": f'hoge={query["hoge"]}, hogeOption={query.get("hogeOption")}',
    }
