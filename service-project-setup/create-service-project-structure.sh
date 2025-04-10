#!/bin/bash

# Prompt the user for the service name
read -p "Enter the service name: " SERVICE_NAME

# Define the base directory using the service name
BASE_DIR=$SERVICE_NAME

# Create the directory structure
mkdir -p $BASE_DIR/{docker,kubernetes/{manifests,helm-charts/templates},configs,service/{scripts,monitoring},scripts/{setup,monitoring,scaling},src,logs,tests,docs}

# Create necessary files in the directories
touch $BASE_DIR/docker/{Dockerfile,docker-compose.yaml}
touch $BASE_DIR/kubernetes/manifests/{deployment.yaml,service.yaml,service-hpa.yaml,configmap.yaml,pvc.yaml,namespace.yaml,monitoring-deployment.yaml,monitoring-service.yaml}
touch $BASE_DIR/kubernetes/helm-charts/templates/{deployment.yaml,service.yaml,hpa.yaml}
touch $BASE_DIR/kubernetes/helm-charts/values.yaml
touch $BASE_DIR/configs/{config.json,environment.env}
touch $BASE_DIR/service/scripts/{init.sh,start.sh,stop.sh,cleanup.sh,backup.sh,restore.sh,scale.sh}
touch $BASE_DIR/service/monitoring/alert-rules.yaml
touch $BASE_DIR/scripts/setup/{cluster.sh,init-storage.sh,monitoring.sh}
touch $BASE_DIR/scripts/monitoring/{setup-prometheus.sh,setup-grafana.sh}
touch $BASE_DIR/scripts/scaling/autoscale.sh
touch $BASE_DIR/logs/logs.log
touch $BASE_DIR/tests/test.yaml
touch $BASE_DIR/src/README.md
touch $BASE_DIR/docs/{architecture.md,monitoring-guide.md,setup-guide.md,usage-guide.md,troubleshooting.md}
touch $BASE_DIR/Makefile
touch $BASE_DIR/README.md

# Output success message
echo "Project structure for '${SERVICE_NAME}' service has been created successfully in the '$BASE_DIR' directory."