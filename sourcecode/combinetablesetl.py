import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())
booksDF = glueContext.create_dynamic_frame.from_catalog(
             database="glue-etl",
             table_name="analysis")

apparelDF = glueContext.create_dynamic_frame.from_catalog(
             database="appareldb",
             table_name="analysis")

# Join both tables on customer_id
booksapparelDF=Join.apply(booksDF, apparelDF, 'customer_id', 'customer_id')

# check the schema of the combined tables
booksapparelDF.printSchema()

# check the count of records
booksapparelDF.count()

# Split the dataFrame to two new column based datasets
colwiseCollection = SplitFields.apply(booksapparelDF,["customer_id","	product_id","product_title"],"productsDF","restDF")
colwiseCollection.keys()

#Check the schema after column split 
colwiseCollection.select("productsDF").printSchema()
colwiseCollection.select("restDF").printSchema()

# split rows based on Star ratings
rowwiseCollection = SplitRows.apply(booksapparelDF,{"star_rating": {">": 3}},"star_rating3above","star_rating3below")
rowwiseCollection.keys()


rowwiseCollection.select("star_rating3below").toDF().select('star_rating').show()
rowwiseCollection.select("star_rating3above").toDF().select('star_rating').show()
 # (or) count

rowwiseCollection.select("star_rating3below").toDF().select('star_rating').count()
rowwiseCollection.select("star_rating3above").toDF().select('star_rating').count()


# Extras
# Union method to merge star_rating3below and star_rating3above 
star_rating3below = rowwiseCollection.select("star_rating3below").toDF()
star_rating3above = rowwiseCollection.select("star_rating3above").toDF()
allstar_ratingDF = star_rating3above.union(star_rating3below)
allstar_ratingDF.show()