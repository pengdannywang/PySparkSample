from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation
from pyspark.sql import Row
from basicex import *
import numpy as np
from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .appName("LinearRegressionWithElasticNet")\
        .config("spark.master","local[*]")\
        .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
textfile = spark.sparkContext.textFile("../logs/api_traffic.log")

df=textfile.toDF()
df.show()
