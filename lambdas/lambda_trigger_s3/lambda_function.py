import json
import boto3

s3 = boto3.resource("s3")


def lambda_handler(event, context):

    s3_record = event["Records"][0]["s3"]
    object = s3.Object(s3_record["bucket"]["name"], s3_record["object"]["key"])
    file_body = object.get()["Body"].read()

    print(file_body)

    return {}
