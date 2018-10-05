from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation
from pyspark.sql import Row
import numpy as np
import re
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Exampe").config("spark.master","local[*]").getOrCreate()

#textfile = spark.sparkContext.textFile("../logs/api_traffic.log")
traffic = spark.read.json("W:/pwang/central_logs/*.txt")
#colldrr=spark.sparkContext.parallelize(traffic.collect())

def parser(line):
    arr=[]
    p=re.compile('(([\\w]+[\\w\\s]*):([\\w\\s]+)[\\w\\s\\.\\=]*(\\:[\\w\\s]+[-0-9\\s\\.\\,]+[-0-9\\s\\.]+)*)|(([\\w]+[\\w\\s]*)=(([\\w\\s]+)([\\w\\.]+)|([\\[]*[\\w\\.\\,\\s]+[\\]*])))') 
    m=p.finditer(line)
    for result in m:
        r=result.group()
        if "Internal API User IP address registry:" not in r:
            arr.append(r)
    return arr
aa=traffic.rdd.flatMap(lambda x:parser(x[7]))
#traffic = spark.read.json("W:/pwang/central_logs/dev.log")
colldrr=spark.sparkContext.parallelize(aa.collect())
print(colldrr.collect())



