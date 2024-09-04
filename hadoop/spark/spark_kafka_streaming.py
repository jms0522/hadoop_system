from pyspark.sql import SparkSession

# SparkSession 생성
spark = SparkSession.builder \
    .appName("KafkaSparkStructuredStreaming") \
    .config("spark.sql.streaming.schemaInference", "true") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2") \
    .getOrCreate()

# Kafka에서 데이터 읽기
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "new_test_topic") \
    .load()

# Kafka value 컬럼을 문자열로 변환
df = df.selectExpr("CAST(value AS STRING)")

# 데이터 콘솔에 출력
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# 쿼리 종료 대기
query.awaitTermination()
