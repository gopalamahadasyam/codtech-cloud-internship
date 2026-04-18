# Task 1 - Cloud Storage Setup
import boto3

# Initialize S3 client
s3 = boto3.client("s3", region_name="us-east-1")

BUCKET_NAME = "codtech-storage-gopalakrishna-2025"

# Create bucket
def create_bucket():
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f"Bucket {BUCKET_NAME} created")

# Upload file
def upload_file(filename):
    s3.upload_file(filename, BUCKET_NAME, filename)
    print(f"Uploaded {filename} to {BUCKET_NAME}")

# List files
def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    for obj in response.get("Contents", []):
        print(obj["Key"])

if __name__ == "__main__":
    list_files()
