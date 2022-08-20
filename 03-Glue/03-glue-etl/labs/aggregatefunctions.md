# Data Transformation and ETL
## JOINS

# Aggregate Functions Exercise

---
**Prerequisite**
Create a new S3 Output Bucket for the output data to be saved to or create a `outputs` folder in the same initial bucket
For this lab I am going to use the same s3 bucket with outputs folder to save the output data from Glue Studio.

---
`Bucket-Name: amazon-dataset-reviews-thulasi`
`output-Folder: outputs`

## Prerequisite

* Make sure you have completed `01-gluecrawler` lab and have your books data in the data catalog
* Similarly create the data catalog for the apparel dataset copied from the `Amazon Reviews Dataset`

### Create dev endpoint
 * Select **Dev Endpoints** in the left hand side pane and click on add endpoint
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl1.png?raw=true)

* Give a new to the endpoint and the role  and click on next eg: glue-etl-endpint, AWSGlueServiceRole-glue-etl-role
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl2.png?raw=true)

* skip network configuration as we are not going to run the notebook inside a VPC for this lab. Click Next
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl3.png?raw=true)

* You can upload your local machine ssh key to access it locally. For the sake of this lab I am skipping this and click on Next and create endpoinot
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl4.png?raw=true)

* It take few minutes for the endpoint to be ready and it will shown as "PROVISIONING"
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl6.png?raw=true)

* READY State
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl7.png?raw=true)

* Select the created endpoint and in Actions dropdown select `Create SageMaker Notebook`
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl8.png?raw=true)

* Give the name for Notebook and respective role (either create new or select existing role with required S3 premissions). Skip rest of the options as defaults and click on Create.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl9.png?raw=true)

* Wait untill the notebook moves from Starting to READY state
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl10.png?raw=true)

READY State
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl11.png?raw=true)

* Goto the AWS Glue console, click on the Notebooks option in the left menu, then select the notebook and click on the Open notebook button.
* On the next pop-up screen, click the OK button. It will open jupyter notebook in a new browser window or tab. In the notebook window, click on Sparkmagic (PySpark) option under the New dropdown menu.
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl2.png?raw=true)

* Rename the note book to `glue-pyspark-lab-aggregatefunctions`
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl3.png?raw=true)  

* It will open notebook file in a new browser window or tab. Copy and paste the following PySpark snippet  to the notebook cell and click Run. It will create Glue Context. The Glue context connects with the Spark session and also provides access to the data lake catalog tables.

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

glueContext = GlueContext(SparkContext.getOrCreate())

```

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl14.png?raw=true)

* It takes some time to start SparkSession and get Glue Context. Wait for the confirmation message saying SparkSession available as ‘spark’.
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl15.png?raw=true)

* Copy the following PySpark snippet in the notebook cell and click Run. Wait for the execution to finish. It will load dynamicframe for the data catalog table `analysis`  in the database `glue-etl`(books review dataset)
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl16.png?raw=true)

* You can check the Schema by running 
  
`booksDF.printSchema()`

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl17.png?raw=true)

`booksDF.count()`

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl18.png?raw=true)


### Describe

* You can use describe method to see statistics of a particular column. The method is generally used with numeric columns or features. Run the following PySpark code snippet to check statistics of the product_title column.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/func1.png?raw=true)

You can also use groupby method with a particular column along with individual aggregation function. Run the following PySpark code snippet to see count per star_rating.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/func2.png?raw=true)

* Run the following PySpark code snippet one by one to see min,max,mean and sum of customer_id per product_title.

### Min
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/func3.png?raw=true)

### Max

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/func4.png?raw=true)

### Mean

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/func5.png?raw=true)

### Sum

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/func6.png?raw=true)


### Orderby

You can use orderBy method to sort Dataframe for a particular column in ascending or descending order. Run the following PySpark code snippet one by one to sort the Dataframe by total_votes first ascending or descending.


![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/func7.png?raw=true)
