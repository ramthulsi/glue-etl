# 1. AWS ETL Lab with [Amazon Customer Reviews Dataset]

## Create S3 bucket to host the dataset

### Choose the bucket name  and select Region where you want to creat your bucket
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/s3bucketcreation/s3bucket1.png?raw=true)

![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/s3bucketcreation/s3bucket.png?raw=true)


### Review details and create bucket
![alt text](https://github.com/Ramthulasi/freelancer-amazon-reviews-dataset-etl-lab/blob/main/screenshots/s3bucketcreation/s3bucket2.png?raw=true)


## Downloading the dataset
```

# Copy the dataset to local machine

mkdir aws-etl-lab
cd aws-etl-lab
aws s3 cp s3://amazon-reviews-pds/tsv/ . --recursive


# Copy the dataset to your S3 bucket

aws s3 cp . s3://{BUCKETNAME} --recursive  # Use default AWS credentials
aws s3 cp . s3://{BUCKETNAME} --recursive --profile {PROFILENAME} #If you have more than one AWS credentials

```

