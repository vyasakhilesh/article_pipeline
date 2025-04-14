from pyspark.sql import SparkSession
from delta import DeltaTable

# Set up Spark session with Delta Lake support
spark = SparkSession.builder \
    .appName("MinIO-Spark-Delta") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.hadoop.fs.s3a.endpoint", "http://localhost:9000") \
    .config("spark.hadoop.fs.s3a.access.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.secret.key", "minioadmin") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .getOrCreate()

# Define S3 bucket location
s3_path = "s3a://my-bucket/delta-table"

# Sample DataFrame
data = [
    (1, "Alice", 25),
    (2, "Bob", 30),
    (3, "Charlie", 35)
]

df = spark.createDataFrame(data, ["id", "name", "age"])

# Write data to Delta Lake on MinIO
df.write.format("delta").mode("overwrite").save(s3_path)

# Read data from Delta Lake on MinIO
df_read = spark.read.format("delta").load(s3_path)
df_read.show()

spark.stop()

