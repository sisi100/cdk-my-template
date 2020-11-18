def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "headers": {
            "Content-Disposition": 'attachment;filename="hoge.txt"',
            "Content-Type": "text/plain",
        },
        "body": "hogehogeなのだよ",
    }
