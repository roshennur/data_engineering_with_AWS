<h1 align="center">Streaming sample data to Amazon Kinesis with Amazon Kinesis Data Generator (KDG)</h1>
<h2>Configuring Kinesis Data Firehose for streaming delivery to Amazon S3</h2>
<h3>Kinesis service -> Amazon Data Firehose -> Create Firehose Stream</h3>
<p align="left">
  <img src="screenshots/1.png" width="1000" height="600"/>
</p>
<h3>Source: Direct Put -> Destination: Amazon s3 -> provide Firehose stream name</h3>
<p align="left">
  <img src="screenshots/2.png" width="1000" height="600"/>
</p>
<h3>Destination settings: select s3 bucket landing zone we created before -> provide prefix as pic for s3 bucket prefix and for s3 bucket error output prefix</h3>
<p align="left">
  <img src="screenshots/3.png" width="1000" height="600"/>
</p>
<h3>Buffer size: 1MB -> Buffer interval -> 60sec -> leave other settings as default -> Create delivery stream</h3>
<p align="left">
  <img src="screenshots/4.png" width="1000" height="600"/>
</p>
<h2>Configuring Amazon Kinesis Data Generator (KDG)</h2>
<h3>Open the KDG help page in browser https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html -> Create Cognito User with CloudFormation</h3>
<p align="left">
  <img src="screenshots/5.png" width="1000" height="600"/>
</p>
<h3>Create stack page -> leave as default -> Next</h3>
<p align="left">
  <img src="screenshots/6.png" width="1000" height="600"/>
</p>
<h3>Specify stack details: provide username and password -> Next</h3>
<p align="left">
  <img src="screenshots/7.png" width="1000" height="600"/>
</p>
<h3>Configure stack options -> leave as default -> Next</h3>
<p align="left">
  <img src="screenshots/8.png" width="1000" height="600"/>
</p>
<h3>Submit the stack</h3>
<p align="left">
  <img src="screenshots/9.png" width="1000" height="600"/>
</p>
<h3>once stack has been successfully deployed -> Outputs tab -> click KinesisDataGeneratorUrl value -> enter username & password -> set Region as yours aws account -> copy template code from github file: template</h3>
<p align="left">
  <img src="screenshots/10.png" width="1000" height="600"/>
</p>
<h3>for strea/delivery stream -> select the Kinesis Data Firehose stream we created -> Records per second: 10 -> click send data -> wait KDG to send data for at least 3000-6000 records</h3>
<p align="left">
  <img src="screenshots/11.png" width="1000" height="600"/>
</p>
