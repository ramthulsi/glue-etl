import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())

booksDF = glueContext.create_dynamic_frame.from_catalog(
             database="glue-etl",
             table_name="analysis"))


booksDF.printSchema()
booksDF.count()

highratingsbooksDF = Filter.apply(booksDF, f = lambda x: x["sales"] >  12000)
highratingsbooksDF.toDF().show()