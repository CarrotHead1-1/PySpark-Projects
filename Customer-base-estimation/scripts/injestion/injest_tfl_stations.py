
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp, input_file_name

spark = SparkSession.builder.appName("IngestTFL").getOrCreate()

RAW_PATH = "/rawData/tflStations.csv"
BRONZE_PATH = "/datalakehouse/bronze/tfl"

df = (spark.read.option("header", True).csv(RAW_PATH)
    .withColumn("ingest_timestamp", current_timestamp())
    .withColumn("source_file", input_file_name())
)

(df.write.format("parquet").mode("overwrite").save(BRONZE_PATH))

