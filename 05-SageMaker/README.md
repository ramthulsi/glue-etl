# Introduction
* * Amazon SageMaker is an end-to-end machine learning platform that lets you build, train, and deploy machine learning models in AWS. It is a highly modular service that lets you use each of these components independently of each other.

### You will Learn:

* * How to use the Jupyter notebook component of Sagemaker to integrate with the data lake using Athena
Populate data frames for data manipulation.

## Create Amazon SageMaker Notebook Instance
* * Go to the Amazon Sagemaker from AWS console


![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage1.png?raw=true)

* * In the Amazon SageMaker navigation pane, click Notebook instances and Click Create notebook instance
 ![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage2.png?raw=true)

### Put following values to create instance
* * Give your choice of name for Notebook instance name e.g., `glue-etl-notebook`
* * You can leave Notebook instance type as default value ml.t2.medium for this lab
* * Leave Elastic Inference as null. This is to add extra resources.
* * Choose a role for the notebook instances in Amazon SageMaker to interact with Amazon S3. As role doesn’t exist select the Create new role option.
* * In Create an IAM Role pop up window, choose the specific S3 bucket you will grant access to. For this lab, choose Any S3 bucket as shown below and click Create Role:
 
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sagen.png?raw=true)

* Click Create notebook instance.
  
*  You will see a Role got create, as you are going to Access Athena from SageMaker, so SageMaker execution role must have the necessary permission to access Athena. To achieve that click the link for newly created IAM Role and in the new window

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage3.png?raw=true)

* * There is no Athena permission available in your SageMaker execution role. In this case, it is “AmazonSageMaker-ExecutionRole-20210927T014192”.
* 
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage4.png?raw=true)

Click Attach Policies button in Permissions tab.
* * Filter policies by “Athena”, check AmazonAthenaFullAccess managed policy and click Attach Policy button at the bottom of the screen. Close the new window/tab.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage5.png?raw=true)


![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage5.png?raw=true)

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage6.png?raw=true)

* * Wait for the notebook instances to be created and the Status to change to Inservice and Click Open Jupyter in from “Actions” column.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage7.png?raw=true)


The notebook interface opens in a separate browser window.


![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage8.png?raw=true)


## Connect the SageMaker Jupyter notebook to Athena
In the Jupyter notebook interface, click New. For the kernel, choose conda_python3


![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage9.png?raw=true)

* * Within the notebook, execute the following commands to install the Athena JDBC driver and in the top toolbar, click Run. (PyAthena is a Python DB API 2.0 (PEP 249) compliant client for the Amazon Athena JDBC driver.)

```
import sys
!{sys.executable} -m pip install PyAthena
```

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage10.png?raw=true)

You can load Athena table data from data lake to Pandas data frame and apply machine learning. 

Your Athena Database name, this is the Glue Database name which you created during previous lab e.g., `glue-etl`. Update the S3 bucket location , so that it looks like `s3://amazon-dataset-reviews-thulasi/athenaquery/`.

```

from pyathena import connect
import pandas as pd
conn = connect(s3_staging_dir='s3://amazon-dataset-reviews-thulasi/athenaquery/',
region_name='us-west-2')

df = pd.read_sql('SELECT * FROM "glue-etl"."analysis" order by total_votes limit 10;', conn)
df

```

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage11.png?raw=true)

### You can also do some analysis and ploting with matplotlib
```
df = pd.read_sql('SELECT total_votes, \
       review_date, \
       count(*) as ratings, \
       avg(star_rating) as avg_star_rating \
       FROM "glue-etl"."analysis" \
       group by 1,2 \
       order by 1,2 limit 500;', conn)
df
```

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage12.png?raw=true)


```
import matplotlib.pyplot as plt 
df.plot(x='review_date',y='avg_star_raging')

```

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/sagemaker/sage13.png?raw=true)


## Cleanup:
- Go to SageMaker Notebook Instances console
- Select the notebook instance that you created e.g. `glue-etl-notebook`
- Choose Actions → Stop, it will take few minutes for the notebook instance to stop.
- Once the notebook instance is stopped, choose Actions → Delete and choose Delete in the confirmation pop-up to delete the instance.