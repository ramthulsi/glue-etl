import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())

# load books dataframe
booksDF = glueContext.create_dynamic_frame.from_catalog(
             database="glue-etl",
             table_name="analysis")

booksDF = booksDF.toDF()
booksDF.show()
#crosstab
booksDF.crosstab('product_title', 'total_votes').show()

#Describe
booksDF.describe('product_title').show()

#groupby
booksDF.groupby('star_rating').count().show()


booksDF.select("customer_id","product_title").groupby('customer_id').min().show()
booksDF.select("customer_id","product_title").groupby('customer_id').max().show()
booksDF.select("customer_id","product_title").groupby('customer_id').mean().show()
booksDF.select("customer_id","product_title").groupby('customer_id').sum().show()

#Orderby

booksDF.orderBy(booksDF.total_votes).show()
booksDF.orderBy(booksDF.total_votes.desc()).show()