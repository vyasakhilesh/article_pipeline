# Define the path to the start service script
START_SCRIPT = ./service/scripts/start.sh

# Define common commands
DOCKER_COMPOSE = docker-compose -f ./airflow-service-docker/docker-compose.yaml
# Default target
.PHONY: all
all: start

# Start the service using the script
.PHONY: start
start:
	@echo "Starting the service using the start script..."
	$(DOCKER_COMPOSE) up -d

.PHONY: rebuild
rebuild:
	@echo "Rebuild and start the service using the start script..."
	$(DOCKER_COMPOSE) up -d --build --force-recreate

# Stop the Docker services
.PHONY: stop
stop:
	@echo "Stopping the Docker services..."
	$(DOCKER_COMPOSE) down

# Restart the service
.PHONY: restart
restart:
	@echo "Restarting the service..."
	$(MAKE) stop
	$(MAKE) start

# Check the status of the services
.PHONY: status
status:
	@echo "Displaying the status of the services..."
	$(DOCKER_COMPOSE) ps

# Clean Docker resources (optional)
.PHONY: clean
clean:
	@echo "Cleaning up unused Docker resources..."
	docker system prune -f