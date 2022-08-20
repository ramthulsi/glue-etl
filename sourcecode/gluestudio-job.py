import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="glue-etl", table_name="analysis", transformation_ctx="S3bucket_node1"
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("marketplace", "string", "marketplace", "string"),
        ("customer_id", "long", "customer_id", "double"),
        ("review_id", "string", "review_id", "string"),
        ("product_id", "string", "product_id", "string"),
        ("product_parent", "long", "product_parent", "long"),
        ("product_title", "string", "product_title", "varchar"),
        ("product_category", "string", "product_category", "string"),
        ("star_rating", "long", "star_rating", "tinyint"),
        ("helpful_votes", "long", "helpful_votes", "long"),
        ("total_votes", "long", "total_votes", "tinyint"),
        ("vine", "string", "vine", "string"),
        ("verified_purchase", "string", "verified_purchase", "string"),
        ("review_headline", "string", "review_headline", "string"),
        ("review_body", "string", "review_body", "string"),
        ("review_date", "string", "review_date", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://amazon-dataset-reviews-thulasi/outputs/",
        "partitionKeys": [],
    },
    transformation_ctx="S3bucket_node3",
)

job.commit()
