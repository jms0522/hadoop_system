from pyspark.sql import SparkSession

if __name__ == "__main__":
    # SparkSession 생성
    spark = SparkSession.builder \
        .appName("Kafka Spark Structured Streaming") \
        .master("local[*]") \
        .getOrCreate()

    # Kafka에서 데이터 스트림 읽기
    kafka_df = spark.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "43.203.192.149:9092") \
        .option("subscribe", "new_test_topic") \
        .load()

    # Kafka에서 가져온 데이터를 문자열로 변환
    kafka_df = kafka_df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")

    # 콘솔에 데이터 출력
    query = kafka_df.writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    # 스트리밍 쿼리 대기
    query.awaitTermination()
