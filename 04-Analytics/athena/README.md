# In this lab, you will complete the following tasks:

* * Query data and create a view with Amazon Athena
* * Athena Workgroups to Control Query Access and Costs
* * Build a dashboard with Amazon QuickSight

---
**Note:**
This lab section is to demonstrate how Athena has a datastore for Glue.
How to use Athena to ondemand Quering on the Glue datastore.
Create views and do analysis, explained with simple sample queries. You can execute complex queries based on your needs and data.


---
## Query Data with Amazon Athena
### In the AWS services console, search for Athena.

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/athena/athena1.png?raw=true)

* * In the Query Editor, select  select the database `glue-etl` that was created from Glue Catalog.
* * Click the table named `analysis` to inspect the fields.
Note: The type for fields id, sporting_event_id and ticketholder_id should be (double).

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/athena/athena2.png?raw=true)

### log the query results to S3

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/athena/athena3.png?raw=true)


### Top 10 Books based on Votes
* Run below query to get the top 10 books based on voting

```
select product_title, total_votes from analysis order by total_votes desc limit 10;

```

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/athena/athena4.png?raw=true)

### Create a view with top ratings
* Run below query to get the best rating books with the star ratings of >=4

```
 select * from analysis where star_rating >= 4;

```

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/athena/athena5.png?raw=true)

As shown above Click Create and then select Create view from query

Name the view `toprated-books` and click Create

* Review the view created in the left pane

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/athena/athena6.png?raw=true)

* Please feel free to explore Athena for on-demand quering