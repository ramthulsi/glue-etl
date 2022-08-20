# GlueStudio Exercise

---
**Prerequisite**
Create a new S3 Output Bucket for the output data to be saved to or create a `outputs` folder in the same initial bucket
For this lab I am going to use the same s3 bucket with outputs folder to save the output data from Glue Studio.

---
`Bucket-Name: amazon-dataset-reviews-thulasi`
`output-Folder: outputs`



### In the left navigation pane, under ETL, click AWS Glue Studio.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/gluestudio/studio1.png?raw=true)

### Click on View Jobs

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/gluestudio/studio2.png?raw=true)


* * * Select the Data source - S3 bucket at the top of the graph.

* * * In the panel on the right under “Data source properties - S3”, choose the `glue-etl` database from the drop down.

* * * For Table, select the `analysis` table.
  
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/gluestudio/studio3.png?raw=true)


### Select the ApplyMapping node. In the Transform panel on the right and change the data type of `customer_id` column to double in the dropdown.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/gluestudio/studio4.png?raw=true)


* Select the Data target - S3 bucket node at the bottom of the graph, and change the Format to `JSON` in the dropdown. Please feel free to playaround with the types, drop the columns etc for transformation output.

* Under “S3 Target Location”, select “Browse S3” browse to the “amazon-dataset-reviews-thulasi” bucket, select “outputs folder” item and press “Choose”.

or add the bucket path

`s3://amazon-dataset-reviews-thulasi/outputs/`

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/gluestudio/studio5.png?raw=true)


* Finally, select the Job details tab at the top. Enter `glue-etl-lab-studio` under Name.

* For IAM Role, since the output folder is in the same S3 bucket I choose the same role that I used for Crawler. Pleae feel free to create a new role with new permissions or update the same role with the new s3 bucket

* Scroll down the page and under Job bookmark, select Disable in the drop down. 

---
**Note**
Glue ETL writes the multipart upload output files based on the number of workers defined in the job. If you need large files keep the number of workers low(minimum is 2)

---

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/gluestudio/studio6.png?raw=true)

Press the Save button in the top right-hand corner to create the job.

Once you see the Successfully created job message in the banner, click the Run button to start the job.

Select Jobs from the navigation panel on the left-hand side to see a list of your jobs.

Select Monitoring from the navigation panel on the left-hand side to view your running jobs, success/failure rates and various other statistics.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/gluestudio/studio8.png?raw=true)

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/gluestudio/studio9.png?raw=true)