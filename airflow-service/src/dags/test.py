from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 4, 14),
    "retries": 0
}

dag = DAG(
    "spark_minio_pipeline",
    default_args=default_args,
    schedule=None
)

spark_task = SparkSubmitOperator(
    task_id="run_spark_job",
    application="/opt/airflow/dags/test_spark_job.py",
    conn_id="spark_default",
    executor_memory="1g",
    executor_cores="1",
    packages="io.delta:delta-spark_2.12:3.3.1",
    dag=dag
)

spark_task