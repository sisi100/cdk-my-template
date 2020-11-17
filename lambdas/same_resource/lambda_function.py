import json
import os
from datetime import datetime

import boto3

s3 = boto3.resource("s3")


def lambda_handler(event, context):

    bucket_name = os.getenv("PUT_BUCKET_NAME")
    key = f"{datetime.now()}.json"

    object = s3.Object(bucket_name, key)
    object.put(Body=json.dumps(event))

    return {}
