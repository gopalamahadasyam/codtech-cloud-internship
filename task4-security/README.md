# CODTECH Task 4 - Cloud Security Implementation

## 1. IAM Configuration
- Created groups: CodtechReadOnly, CodtechDevelopers
- Applied least-privilege principle
- Created codtech-dev-user and added to Developers group
- Custom policy restricts S3 access and blocks bucket deletion

## 2. Secure Storage
- Public access completely blocked on S3 bucket
- Bucket versioning enabled
- Object-level logging enabled via CloudTrail

## 3. Data Encryption
- Server-Side Encryption AES-256 enabled on S3
- KMS key created for advanced encryption
- All data encrypted at rest

## 4. Audit and Compliance
- CloudTrail enabled for all API activity logging
- Multi-region trail active
- Logs stored securely in encrypted S3 bucket

## 5. Security Best Practices Applied
- Principle of Least Privilege
- Encryption at Rest
- Full Audit Trail
- No public bucket access
