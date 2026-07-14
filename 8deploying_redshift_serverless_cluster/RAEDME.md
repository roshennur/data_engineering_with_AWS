<h1 align="center">Deploying Redshift Serverless cluster and running Redshift Spectrum queries.</h1>
<p>In this section we're going to create a new Redshift Serverless cluster and configure Redshift Spectrum so that we can query data in external tables on Amazon S3.</p>
<h2>Uploading sample data to Amazon S3</h2>
<h3>Download the generic data named "user_details.csv" from dataset folder -> Amazon S3 service -> dataeng-landing-zone -> create folder "users" -> upload csv file in it</h3>
<p align="left">
  <img src="screenshots/1.png" width="1000" height="600"/>
</p>
<h2>Let's create Role for Redshift</h2>
<h3>AWS IAM -> Roles -> Create role -> select AWS service -> Use case: Redshift -> Redshift - customizable -> Next</h3>
<p align="left">
  <img src="screenshots/2.png" width="1000" height="600"/>
</p>
<h3>Attach 4 folliwing policies -> provide Role name: AmazonRedshiftSpectrumRole</h3>
<p align="left">
  <img src="screenshots/3.png" width="1000" height="600"/>
</p>
<h2>Creating a Redshift cluster</h2>
<h3>Amazon Redshift -> Try Redshift Serverless free trial -> Configuration: Use default settings</h3>
<p align="left">
  <img src="screenshots/4.png" width="1000" height="600"/>
</p>
<h3>Associated IAM roles -> select AmazonRedshiftSpectrumRole -> click Associate IAM role -> select the role associated -> Set default -> Make default -> Confirm</h3>
<p align="left">
  <img src="screenshots/5.png" width="1000" height="600"/>
</p>
<h3>Save configuration -> this will create Amazon Redshift Cluster</h3>
<p align="left">
  <img src="screenshots/6.png" width="1000" height="600"/>
</p>
<h2>Now let's query data in the data lake with Redshift Spectrum</h2>
<h3>Amazon Redshift Serverless dashboard -> Query data -> Query editor v2</h3>
<p align="left">
  <img src="screenshots/7.png" width="1000" height="600"/>
</p>
<h3>Connect to defoult workgroup we created -> federated user -> Create connection</h3>
<p align="left">
  <img src="screenshots/8.png" width="1000" height="600"/>
</p>
<h3>in the database dropdown change db to dev, so our new schema is created in the db called dev</h3>
<p align="left">
  <img src="screenshots/9.png" width="1000" height="600"/>
</p>
<h3>run the following command to create external schema called spectrum_schema and also to create a new db in the Glue Data Catalog called users</h3>
<p align="left">
  <img src="screenshots/10.png" width="1000" height="600"/>
</p>
<h3>we can now define external table that will be registered in the Glue Data Catalog under our users database in Glue and in the spectrum_schema in Redshift</h3>
<p align="left">
  <img src="screenshots/11.png" width="1000" height="600"/>
</p>
<h3>we can see the schema we created by pressing refresh button on the left </h3>
<p align="left">
  <img src="screenshots/12.png" width="1000" height="600"/>
</p>
<h3>or we can query the sample of it to see dataset</h3>
<p align="left">
  <img src="screenshots/13.png" width="1000" height="600"/>
</p>
