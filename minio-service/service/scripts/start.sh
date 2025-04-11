#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Navigate to the directory containing the docker-compose.yml file
cd ./minio-docker/

# Pull the latest images (optional, if needed)
echo "Pulling the latest Docker images..."
docker-compose build 

# Start the service(s)
echo "Starting the Docker services..."
docker-compose up -d --force-recreate

# Confirm the services are running
echo "Checking the status of the services..."
docker-compose ps

echo "All services are up and running!"