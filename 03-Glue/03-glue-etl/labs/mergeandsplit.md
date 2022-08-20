# Data Transformation and ETL
## JOINS

# Merge and Split Exercise

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

* Rename the note book to `glue-pyspark-lab`
  
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


## Merge & Split Data Sets
* When creating ETL job, generally you work with more than one data sets and transformation with them. The transformation could be like merging the two data sets together or split one data set into two or more data sets. In this task, you will learn to merge and split data sets.



* Run the following PySpark code snippet which loads data in the Dynamicframe from the `appareldb` and `glue-etl` databases in the `analysis` table.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl20.png?raw=true)

* Run the following PySpark code snippet one by one to check schema of the two Dynamicframes. You will find that the frames have customer_id as common key or field. You can join the booksDFDF and apparelDF Dynamicframes based on the field customer_id.

* Run the following PySpark code snippet to join the booksDFDF and apparelDF Dynamicframes based on the field customer_id. Use printSchema method  and count method to check the schema of the merged frame and also new count of records.
  
* ---
**Note:**
If the size fo the data is large you might get memory limit exceeded error in the notebook. Make sure you use the right notebook instance base on your size of dataset.

---

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl21.png?raw=true)

* If you can see two columns customer_id and .customer_id due to join on the key. You can use drop_fields method to remove .customer_id field.

* You can split a Dynamicframe vertically based on the columns. Use SplitFields method which splits a Dynamicframe into a collection of Dynamicframes. Run the following PySpark code snippet to split booksDFDF frame into two frames productsDF and restDF. The productsDF has three columns customer_id,product_id and product_title. The restDF will have the remaining of the columns. You can use the keys method to check creation of the Dynamicframe in the Dynamicframe collection colwiseCollection.
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl022.png?raw=true)

* Run the following PySpark code snippet one by one to check schema of the two Dynamicframes productsDF and restDF.
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl22.png?raw=true)


* Similar to the column wise split, you can split a Dynamicframe horizontally based on the row. Use SplitRows method which splits a Dynamicframe into a collection of Dynamicframes based on the condition specified for the rows. Run the following PySpark code snippet to split booksDF frame into two frames ratings3above and ratings3below. Both frames have the same columns but one has rows with ratings values above 3 and other has rows with ratings value lower than 3. You can use the keys method to check creation of the Dynamicframe in the Dynamicframe collection rowwiseCollection
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl23.png?raw=true)

* Run the following PySpark code snippet one by one to check the top 20 values of the star_rating column in the two Dynamicframes star_rating3above and star_rating3below.
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl24.png?raw=true)

* Count
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/etl-labs/etl25.png?raw=true)



* You learnt about manipulating data in and across Dataframes in the workshop so far