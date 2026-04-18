# CODTECH Task 3 - Multi-Cloud Architecture

## Architecture
User Request -> AWS API Gateway -> AWS Lambda -> Response

## Live API URL
https://hf5dgddg1i.execute-api.us-east-1.amazonaws.com/prod/

## AWS Services Used
- AWS Lambda: Serverless compute
- AWS API Gateway: Public HTTP endpoint
- AWS IAM: Role and permissions

## GCP Equivalent Services
- GCP Cloud Functions: Equivalent to AWS Lambda
- GCP Cloud Endpoints: Equivalent to API Gateway
- GCP IAM: Role and permissions

## Interoperability
- AWS Lambda can call GCP Cloud Functions via HTTPS
- Both platforms support REST APIs for cross-cloud communication
- Data flows between clouds using standard HTTP/JSON

## Test Result
{"source": "AWS Lambda", "message": "Multi-cloud architecture working!", "aws_service": "Lambda", "gcp_service": "Cloud Functions"}