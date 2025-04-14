from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 4, 14),
    "retries": 1
}

dag = DAG(
    "spark_minio_pipeline",
    default_args=default_args,
    schedule_interval="@daily"
)

spark_task = SparkSubmitOperator(
    task_id="run_spark_job",
    application="/opt/spark/spark_job.py",
    conn_id="spark_default",
    executor_memory="2g",
    executor_cores="1",
    packages="io.delta:delta-core_2.12:2.4.0",
    dag=dag
)

spark_task
