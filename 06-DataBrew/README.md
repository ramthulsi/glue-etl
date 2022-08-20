# DataBrew Lab

- In this lab, we will be using AWS Glue DataBrew to explore a dataset in S3, and to clean and prepare the data.

- To do this, we will first set up an IAM role to use in DataBrew, and an S3 bucket for the results from the DataBrew jobs.

CloudFormation Stack Deployment
Deploy the below template in the region where your S3 bucket is located.

```
File Location:

cloudformation/databrewlab.yaml

Enter Parameters: (Below are mine, please enter yours accordingly)

SourceBucket: "amazon-dataset-reviews-thulasi"
SourceKey: "analysis/amazon_reviews_us_Books_v1_02.tsv.gz"

```

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew1.png?raw=true))


![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew2.png?raw=true)


- Check the box “I acknowledge that …”, then click on “Create Stack” to create the stack
- Once your stack is deployed, click the Outputs tab to view more information
- Note the values for DatasetS3Path, DataBrewLabRole and DataBrewOutputS3Bucket which will be used in the lab

## Creating a project

### Navigate to the AWS Glue DataBrew service

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew3.png?raw=true)

- On the DataBrew console, select Projects
- 
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew4.png?raw=true)
- 
- Click Create project

* In the Project details section, enter `glue-etl-databrew` as the project name

In the Select a dataset section, select New dataset and enter `glue-etl-databrew-amazonbooksreview`

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew5.png?raw=true)

In the Connect to a new dataset section, select Amazon S3 under “Data lake/data store”

Enter the DatasetS3Path that is available in Event Engine Team Dashboard or outputs section of your CloudFormation stack

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew6.png?raw=true)


![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew7.png?raw=true)


In the Sampling section, leave the default configuration values

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew8.png?raw=true)


In the Permissions section, select the role databrew-lab-DataBrewLabRole-xxxxx from the drop-down list

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew9.png?raw=true)

Click Create project
Glue DataBrew will create the project, this may take a few minutes.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew10.png?raw=true)

### Exploring the dataset.
- When the project has been created, you will be presented with the Grid view. This is the default view, where a sample of the data is shown in tabular format.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brewg.png?raw=true)


- The Grid view shows

  - Columns in the dataset
  - Data type of each column
  - Summary of the range of values that have been found
  - Statistical distribution for numerical columns

- Click on the Schema tab

- The Schema view shows the schema that has been inferred from the dataset. In schema view, you can see statistics about the data values in each column.

- In the Schema view, you can

   - Select the checkbox next to a column to view the summary of statistics for the column values
   - Show/Hide columns
   - Rename columns
   - Change the data type of columns
   - Rearrange the column order by dragging and dropping the columns
   - 
- Click on the Profile tab

 - In the Profile view, you can run a data profile job to examine and collect statistical summaries about the data. A data    profile is an assessment in terms of structure, content, relationships, and derivation.
  
 - Click on Run data profile
  
 - In the job details and job run sample panels, leave the default values.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew11.png?raw=true)

- In the Job output settings section, select the S3 bucket with the name databrew-lab-databrewoutputs3bucket-xxxxx and a folder name (eg. data-profile)

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew12.png?raw=true)

  - In the Permissions section, select the IAM role with the name databrew-lab-DataBrewLabRole-xxxxx

  - Leave all other settings as the default values

  - Click Create and run job

  - The data profile job takes approximately 5 minutes complete. You can continue with the rest of the labs from step 15 below while you wait, and retun to the following steps to examine the profile of the dataset.

## - Click on Jobs from the menu on the left hand side of the DataBrew console.

  - Click on Profile jobs tab to view a list of profile jobs.

  - You can see the status of your profile job on this screen.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew13.png?raw=true)

* When the profile job has successfully completed, click on View data profile
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew14.png?raw=true)
  
- You can also access the data profile from the Profile tab in the project.

- The data profile shows a summary of the rows and columns in the dataset, how many columns and rows are valid, and correlations between columns.

## Click on the Column statistics tab to view a column-by-column breakdown of the data values.

 ![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew15.png?raw=true)


## Preparing the dataset
* In this section, we will apply the following transformations to the dataset.

  - Convert the review_date column date format form YYYY-MM-dd to month*ddd, *yyyy
  - Split the review_date column into three new columns (year, month, day) to partition the data by these columns
 

- Click on the # icon next to the review_date column name 

 ![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew16.png?raw=true)

- Select Date-time Formats , select format `month*ddd, *yyyy` and apply .

 ![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew17.png?raw=true)

- More Transformations
   - We breakdown the review_date to three columns for Year, date, month


 ![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew18.png?raw=true)

-  After Apply 
-  
 ![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/databrew/brew19.png?raw=true)

 - Please feel free to make your hands dirty by exploring the options in Databrew. Much more can be done with this amazing tool.