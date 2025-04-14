FROM bitnami/spark:latest
# Set environment variables (customize if needed)
ENV SPARK_MASTER_PORT=7077 \
    SPARK_MASTER_WEBUI_PORT=8080 \
    SPARK_WORKER_WEBUI_PORT=8081
# Expose necessary ports
EXPOSE 7077 8080 8081
USER root
RUN install_packages curl
USER 1001
# Install python deps
COPY requirements.txt .
RUN pip3 install -r requirements.txt
