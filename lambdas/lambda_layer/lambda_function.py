import requests


def lambda_handler(event, context):

    url = "https://blog.i-tale.jp/"
    response = requests.get(url)

    return {"text": response.text}
