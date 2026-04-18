import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "source": "AWS Lambda",
            "message": "Multi-cloud architecture working!",
            "aws_service": "Lambda",
            "gcp_service": "Cloud Functions"
        })
    }