<p align="center">
  <img src="miscellaneous/aws_logo.png" width="150"/>
  &nbsp;&nbsp;&nbsp;&nbsp;
  <h1 align="center">Data Engineering with AWS</h1>
</p>
<br>

<h4>Step 1: Create S3 Buckets.</h4>
<p>In this step we will create 3 Amazon S3 buckets for our project by using AWS CLI.</p>
<p>
  <img src="miscellaneous/aws_s3_bucket_setup.png" width="1000"/>
</p>

<h4>Step 2: CSV to Parquet</h4>
<p>We will configure an S3 bucket to automatically trigger a Lambda function whenever a new file is written to the bucket. In the 
   Lambda function we're going to make use of an open-source Python library called AWS SDK for Pandas.</p>
<p>
  <img src="miscellaneous/csv_to_parquet.png" width="1000"/>
</p>

<h4>Step 3: Configuring Lake Formation permissions</h4>
<p>
Third step begins by creating a custom IAM policy based on AmazonAthenaFullAccess and attaching it to a new IAM user called datalake-user. An additional S3 bucket is created to store Athena query results. The user then verifies that they can query tables in the cleanzonedb database. Next, the transitions from IAM-based permissions to AWS Lake Formation permissions. This involves revoking IAMAllowedPrincipals permissions from the cleanzonedb database and its csvtoparquet table, allowing more granular access control through Lake Formation. Finally, column-level permissions are configured for datalake-user. By excluding the favorite_num column, the user can query the table through Athena but can only retrieve the name column.
</p>
<p>
  <img src="miscellaneous/configuring_lake_formation_permissions.png" width="1000"/>
</p>
