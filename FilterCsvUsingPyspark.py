from pyspark.sql import SparkSession

#Initialize SparkSession
spark = SparkSession.builder.appName('TestApp').getOrCreate()

# Load data into a data frame
df = spark.read.csv('path/to/csv/file', header=True, inferSchema=True)

#Filter users older than 25 years
filtered_df = df.filter(df.age<=25)

# Show the results
filtered_df.show()

# Close sparksession
Spark.stop()
