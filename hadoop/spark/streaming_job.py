from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# SparkSession 생성
spark = SparkSession.builder \
    .appName("KafkaStructuredStreaming") \
    .config("spark.sql.streaming.schemaInference", "true") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
    .getOrCreate()

# Kafka에서 데이터 읽기
kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:9092") \
    .option("subscribe", "new_test_topic") \
    .option("startingOffsets", "earliest") \
    .load()

# Kafka에서 읽어온 데이터에서 value 컬럼을 문자열로 변환
value_df = kafka_df.selectExpr("CAST(value AS STRING)")

# 데이터를 HDFS에 저장
query_hdfs = value_df.writeStream \
    .format("parquet") \
    .outputMode("append") \
    .option("checkpointLocation", "hdfs://namenode:9000/user/ubuntu/checkpoint") \
    .option("path", "hdfs://namenode:9000/user/ubuntu/datasets/logs") \
    .start()

query_hdfs.awaitTermination()
