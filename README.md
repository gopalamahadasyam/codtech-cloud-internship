# CODTECH Cloud Computing Internship

Intern: Gopal
Platform: AWS

## Tasks Completed

### Task 1 - Cloud Storage Setup
- Created S3 bucket: codtech-storage-gopalakrishna-2025
- Uploaded sample files
- Enabled versioning and AES256 encryption
- Blocked all public access

### Task 2 - Cloud Monitoring and Alerts
- Launched EC2 instance: i-01b2b0e22aa4aa7e1
- Enabled detailed CloudWatch monitoring
- Created CPU and Status Check alarms
- Set up SNS email alerts
- Created CloudWatch Dashboard

### Task 3 - Multi-Cloud Architecture
- Deployed AWS Lambda function
- Created API Gateway endpoint
- Live API: https://hf5dgddg1i.execute-api.us-east-1.amazonaws.com/prod/
- Documented GCP equivalent services

### Task 4 - Cloud Security Implementation
- Created IAM groups: CodtechReadOnly, CodtechDevelopers
- Created IAM user with least privilege policy
- Enabled S3 encryption with AES256
- Created KMS key: alias/codtech-key
- Enabled CloudTrail for audit logging
- Blocked all public S3 access
