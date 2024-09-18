FROM bitnami/spark:latest

USER root

# 필요한 패키지 설치 (wget 또는 curl)
RUN apt-get update && apt-get install -y wget

# 필요한 JAR 파일 다운로드
RUN wget -P /opt/bitnami/spark/jars/ \
    https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.5.2/spark-sql-kafka-0-10_2.12-3.5.2.jar \
    https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.5.2/kafka-clients-3.5.2.jar

# 권한 설정 (필요한 경우)
RUN chmod a+r /opt/bitnami/spark/jars/*.jar

USER 1001
