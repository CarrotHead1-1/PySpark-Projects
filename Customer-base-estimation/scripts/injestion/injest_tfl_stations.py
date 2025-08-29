
from utlis.sparkSession import get_spark
from pyspark.sql.functions import current_timestamp, input_file_name

RAW_PATH = "Customer-base-estimation/rawData/tflStations.csv"

OUTPUT_PATH = "Customer-base-estimation/datalakehouse/bronze/tfl"

def main():
    spark = get_spark("tflStationsIngest")

    df = (spark.read.option("header", True).csv(RAW_PATH)
          .withColumn("ingest_timestamp", current_timestamp())
          .withColumn("source_file", input_file_name)
        )
    
    (df.write.format("parquet")
     .mode("overwrite")
     .save(OUTPUT_PATH)
    )

    print("Ingestion Complete")

if __name__ == "__main__":
    main()
