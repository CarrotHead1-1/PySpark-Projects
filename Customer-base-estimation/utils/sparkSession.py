
from pyspark.sql import SparkSession

#returns a spark session 
def get_spark(app_name: str = "InjestJiob") -> SparkSession:
    return SparkSession.builder.appName(app_name).getOrCreate()
