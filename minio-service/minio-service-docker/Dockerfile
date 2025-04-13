# Base MinIO image
FROM minio/minio:latest

# Set working directory
WORKDIR /data

# Expose default MinIO ports
EXPOSE 9000 9001

# Start MinIO server in distributed mode (scalable for future use)
CMD ["minio", "server", "/data"]