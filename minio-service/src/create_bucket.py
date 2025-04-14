from minio import Minio
from minio.error import S3Error

# Initialize MinIO client
client = Minio(
    "play.min.io",  # Replace with your MinIO server URL
    access_key="YOUR_ACCESS_KEY",
    secret_key="YOUR_SECRET_KEY",
    secure=True  # Set to False if using HTTP
)

# Bucket name
bucket_name = "my-new-bucket"

# Check if bucket exists
found = client.bucket_exists(bucket_name)
if not found:
    client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' created successfully!")
else:
    print(f"Bucket '{bucket_name}' already exists.")
