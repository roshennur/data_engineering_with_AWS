<h1>Joining datasets with AWS Glue Studio</h1>
<h2>Creating a new data lake zone</h2>
<h3>AWS Console -> Glue -> Databases -> Add Database -> provide DB name -> Create database</h3>
<p align="left">
  <img src="screenshots/1.png" width="1000" height="600"/>
</p>
<h2>Creating new IAM role for the Glue job</h2>
<h3>AWS Console -> IAM -> Policies -> Create policy -> copy the JSON policy code from policies file -> paste -> Next</h3>
<p align="left">
  <img src="screenshots/2.png" width="1000" height="600"/>
</p>
<h3>provide policy name -> Create policy</h3>
<p align="left">
  <img src="screenshots/3.png" width="1000" height="600"/>
</p>
<h3>Roles -> Create role -> Trusted entity: AWS service -> Use case: Glue -> Next</h3>
<p align="left">
  <img src="screenshots/4.png" width="1000" height="600"/>
</p>
<h3>Attach permissions -> select the policy we just created on search bar -> also select policy named: AWSGlueServiceRole -> Next</h3>
<p align="left">
  <img src="screenshots/5.png" width="1000" height="600"/>
</p>
<h3>provide Role name -> Create role</h3>
<p align="left">
  <img src="screenshots/6.png" width="1000" height="600"/>
</p>
