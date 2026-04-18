# Task 4 - Cloud Security Implementation
import boto3

iam = boto3.client("iam")
kms = boto3.client("kms", region_name="us-east-1")
s3 = boto3.client("s3", region_name="us-east-1")

BUCKET_NAME = "codtech-storage-gopalakrishna-2025"

# List IAM groups
def list_groups():
    response = iam.list_groups()
    for group in response["Groups"]:
        print(f"Group: {group["GroupName"]}")

# Check bucket encryption
def check_encryption():
    response = s3.get_bucket_encryption(Bucket=BUCKET_NAME)
    rules = response["ServerSideEncryptionConfiguration"]["Rules"]
    print(f"Encryption: {rules[0]["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"]}")

# List KMS keys
def list_kms_keys():
    response = kms.list_aliases()
    for alias in response["Aliases"]:
        if "codtech" in alias["AliasName"]:
            print(f"KMS Key: {alias["AliasName"]}")

if __name__ == "__main__":
    list_groups()
    check_encryption()
    list_kms_keys()
