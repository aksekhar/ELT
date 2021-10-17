
from pyspark.sql import SparkSession

file="/Volumes/AIML/Learning_Docs/Ml-AI/data_processing/data/signal-data.csv"

if __name__ == '__main__':
    spark = SparkSession.builder.appName('conn_save').getOrCreate()
    ds = spark.read.csv(file, inferSchema=True, header=True)
    ds.show()