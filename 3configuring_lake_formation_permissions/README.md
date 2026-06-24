<h1 align="center">Configuring Lake Formation permissions</h1>
<h2>Creating a new user with IAM permissions</h2>
<h3>On AWS Management Concole, go to the Policies on left-menu, filter in "Athena" and select AmazonAthenaFullAccess policy</h3>
<p align="left">
  <img src="screenshots/1.png" width="1000" height="600"/>
</p>
<h3>Copy all JSON in that policy, and go back to create new policy and paste it on JSON Tab</h3>
<p align="left">
  <img src="screenshots/2.png" width="1000" height="600"/>
</p>
<h3>In a new plocy JSON modify and insert new policies and resource from file policies.json</h3>
<p align="left">
  <img src="screenshots/3.png" width="1000" height="600"/>
</p>
<h3>Once pasted click on Next:Review and enter policy name and click Create Policy</h3>
<p align="left">
  <img src="screenshots/4.png" width="1000" height="600"/>
</p>
<h2>Now lets create new IAM user</h2>
<h3>In the IAM console, click on Users -> Enter user name</h3>
<p align="left">
  <img src="screenshots/5.png" width="1000" height="600"/>
</p>
<h3>Next in Set Permissions: select "Attach ploicies directly" and in searchbox type the policy name we created recently and select -> Next</h3>
<p align="left">
  <img src="screenshots/6.png" width="1000" height="600"/>
</p>
