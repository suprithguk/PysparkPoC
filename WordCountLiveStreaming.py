from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

spark = SparkSession
  .builder
  .appName('')
  .getOrCreate()

lines = spark
  .readStream
  .format('socket')
  .option("host","hostname")
  .option("port","9000")
  .load()

words = lines.select(explode(split(lines.value, '')).alias("word"))

wordCounts = words.groupBy("word").count()
