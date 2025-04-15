FROM apache/airflow:latest-python3.12

USER root
RUN apt-get update && apt-get install -y git procps openjdk-17-jdk && apt-get clean
# Set JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64/
USER airflow
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt