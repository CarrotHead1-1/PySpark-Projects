
from utils.sparkSession import get_spark
from pyspark.sql.functions import current_timestamp, input_file_name


#file paths
RAW_PATH = "Customer-base-estimation/rawData/tflStations.csv"
PARQUET_PATH = "Customer-base-estimation/datalakehouse/bronze/tfl"

def main() -> None:

    spark = get_spark("tflStationsIngest")

    df = (spark.read.option("header", True).csv(RAW_PATH)
          .withColumn("ingest_timestamp", current_timestamp)
          .withColumn("soure_file", input_file_name))

    (df.write.format("parquet")
     .mode("overwrite")
     .save(PARQUET_PATH))

if __name__ == "__main__":
    main()