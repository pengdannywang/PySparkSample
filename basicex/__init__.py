from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .appName("LinearRegressionWithElasticNet")\
        .config("spark.master","local[*]")\
        .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")