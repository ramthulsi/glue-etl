# Data Transformation and ETL

### Create Glue Crawler for raw data load
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue1.png?raw=true)

### On the AWS Glue menu, select Crawlers.
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue2.png?raw=true)

* Click Add crawler.

* Enter ***amazon-glueetl-lab*** as the crawler name for initial data load.

* Optionally, enter the description. This should also be descriptive and easily recognized and Click Next.

### Choose Data stores, Crawl all folders and Click Next

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue3.png?raw=true)


### On the Add a data store page, make the following selections:

* For Choose a data store, click the drop-down box and select S3.

* For Crawl data in, select Specified path in my account.

* For Include path, browse to the target folder stored CSV files, e.g., s3://s3://amazon-dataset-reviews-thulasi/analysis

### Click Next
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue4.png?raw=true)

### On the Add another data store page, select No. and Click Next.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue5.png?raw=true)


### On the Choose an IAM role page, make the following selections:
- Select Choose an existing IAM role.
- For IAM role, Create new I am Role and give it a name. eg: "AWSGlueServiceRole-glue-etl-role"
### Click Next.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue6.png?raw=true)

### On the Create a schedule for this crawler page, for Frequency, select Run on demand and Click Next.
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue7.png?raw=true)

### On the Configure the crawler’s output page, click Add database to create a new database for our Glue Catalogue.

* Enter ***glue-etl*** as your database name and click create
  
* For Configuration options (optional), select "Update the table definition in the data catalog." and keep the remaining default configuration options and Click Next.
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue8.png?raw=true)

### Review the summary page noting the Include path and Database output and Click Finish. The crawler is now ready to run.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue9.png?raw=true)

### Tick the crawler name, click Run crawler button.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue10.png?raw=true)

Crawler will change status from starting to stopping, wait until crawler comes back to ready state (the process will take a few minutes), you can see that it has created glue-etl table and took less than a minute for 1.2GB data.

### In the AWS Glue navigation pane, click Databases > Tables. You can also click the ***glue-etl*** database to browse the tables.
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue11.png?raw=true)


# Data Validation 
### Within the Tables section of your ***glue-etl*** database, click the "analysis" table.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue12.png?raw=true)

You can see that the Glue crawler has created the Schema of the dataset we selected from S3.

# Check Database Schema Details
* Click on Edit Table on the top left corner and you can see all the details of the table like siz, no of records etc.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue13.png?raw=true)


# Change the name of the Column. 
* *Click on the the column you want to edit and save.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue14.png?raw=true)


# Add extra columns
* * Click on Edit Schema on the top right corner and you can add the new column

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/glue15.png?raw=true)

## Monitoring

* You can check the status of the logs of the crawler once the crawler is in ready state

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/glue/gluelogs.png?raw=true)

