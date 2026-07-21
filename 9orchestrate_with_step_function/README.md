<h1 align="center">Orchestrating a data pipeline using AWS Step Functions</h1>
<p>For our Step Function state machine, we will start by running Lambda function that checks the extension of an incoming file to determine the type of file. Once determined, we'll pass that information on to the next state. If it is a file type we 
   support, we'll call a Lambda function to process the file, but if it's not, we'll send out a notification, indication that we can't process the file. Once we've created our state machine, we will configure EventBridge to automatically trigger the state 
   machine when a file is uploaded to a specific Amazon S3 path.
</p>

<h2>Using Lambda function to determine the file extension</h2>
<h3>AWS Lambda -> Create function -> Author from scratch -> provide function name -> Runtime: Python 3.10 -> Create function</h3>
<p align="left">
  <img src="screenshots/1.png" width="1000" height="600"/>
</p>
<h3>in the Code source block -> replace existing code with the code below in picture -> Deploy</h3>
<p align="left">
  <img src="screenshots/2.png" width="1000" height="600"/>
</p>

<h2>Create Lambda to randomly generate failures</h2>
<h3>AWS Lambda -> Create function -> Author from scratch -> provide function name -> Runtime: Python 3.10 -> Create function</h3>
<p align="left">
  <img src="screenshots/3.png" width="1000" height="600"/>
</p>
<h3>in the Code source block -> replace existing code with the code below in picture -> Deploy</h3>
<p align="left">
  <img src="screenshots/4.png" width="1000" height="600"/>
</p>
