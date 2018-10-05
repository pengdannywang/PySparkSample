'''
Created on 28Sep.,2018

@author: pwang
'''
from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation
from pyspark.sql import Row
from basicex import *
import numpy as np
import re
from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .appName("Exampe")\
        .config("spark.master","local[*]")\
        .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")
#textfile = spark.sparkContext.textFile("../logs/api_traffic.log")
log = spark.read.json("W:/pwang/central_logs/kibana.json")
#colldrr=spark.sparkContext.parallelize(traffic.collect())
#log.createOrReplaceTempView("txt")
#sql=spark.sql("select query,split(request_path,'/')[1] as a,split(request_path,'/')[2] as b,split(request_path,'/')[3] as c,split(request_path,'/')[4] as d, * from txt")

        
#sql.select("@timestamp","a","b","c","d","query","remote_addr").where("query is not null").show()
#traffic = spark.read.json("W:/pwang/central_logs/dev.log")
log.show();

