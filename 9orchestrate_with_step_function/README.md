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

<h2>Let's create an SNS topic and subscribing to an email address</h2>
<h3>Amazon SNS -> Topics -> Create topic -> Type: Standard -> provide name -> Create topic</h3>
<p align="left">
  <img src="screenshots/5.png" width="1000" height="600"/>
</p>
<h3>Protocol: email -> Endpoint: provide email address -> Create subscription</h3>
<p align="left">
  <img src="screenshots/6.png" width="1000" height="600"/>
</p>

<h2>Creating a new Step Function state machine</h2>
<h3>AWS Step Function -> State machines -> Create state machine -> select Blank and provide name: ProcessFilesStateMachine -> Continue</h3>
<p align="left">
  <img src="screenshots/7.png" width="1000" height="600"/>
</p>
<h3>Design Tab -> in the left drag AWS Lambda Invoke between start and end block -> provide state name -> for Function name: dataeng-check-file-ext</h3>
<p align="left">
  <img src="screenshots/8.png" width="1000" height="600"/>
</p>
<h3>Flow Tab on left -> drag Choice state between Lambda invoke and End state</h3>
<p align="left">
  <img src="screenshots/9.png" width="1000" height="600"/>
</p>
<h3>Configuration for new chaice state -> click pencil edit icon next to Rule #1 -> Add conditions -> Expression: $states.input.file_extension -> Operator: matches string -> value: .csv -> Save conditions</h3>
<p align="left">
  <img src="screenshots/10.png" width="1000" height="600"/>
</p>
<h3>Actions tab -> drag AWS Lambda Invoke to the left-hand side of the two choice boxes -> APi arguments: dataeng-random-failure function</h3>
<p align="left">
  <img src="screenshots/11.png" width="1000" height="600"/>
</p>
<h3>Flow tab -> drag Pass state to the Default rule box leading from Choice state -> Pass state output: paste following into box </h3>
<p align="left">
  <img src="screenshots/12.png" width="1000" height="600"/>
</p>
<h3>Actions tab -> drag Amazon SNS Publish state below Pass state -> API arguments: dataeng-failure-notification function</h3>
<p align="left">
  <img src="screenshots/13.png" width="1000" height="600"/>
</p>
<h3>click on Process CSV state -> Error handling tab -> Catch errors: click on Add new catcher -> Errors: States.ALL -> Fallback state: SNS Publish </h3>
<p align="left">
  <img src="screenshots/14.png" width="1000" height="600"/>
</p>
<h3>Flow tab -> drag Success state under the Process CSV state -> drag Fail state under the SNS Publish state </h3>
<p align="left">
  <img src="screenshots/15.png" width="1000" height="600"/>
</p>
<h3>Config tab -> provide State machine name -> Confirm</h3>
<p align="left">
  <img src="screenshots/16.png" width="1000" height="600"/>
</p>

<h2>Configure S3 bucket to send events to EventBridge</h2>
<h3>Amazon S3 -> click on dataeng-clean-zone bucket -> Properties tab -> sroll down Event Notifications section -> click Edit button next Amazon EventBridge</h3>
<p align="left">
  <img src="screenshots/17.png" width="1000" height="600"/>
</p>
<h3>click selector for On -> Save Changes</h3>
<p align="left">
  <img src="screenshots/18.png" width="1000" height="600"/>
</p>

<h2>Creating an EventBridge rule for triggering Step Functions state machine</h2>
<h3>Amazon EventBridge -> Rules -> defaould Event Bus -> Create rule</h3>
<p align="left">
  <img src="screenshots/19.png" width="1000" height="600"/>
</p>
<h3>Builder mode: advanced builder -> provide name for rule -> Next</h3>
<p align="left">
  <img src="screenshots/20.png" width="1000" height="600"/>
</p>
<h3>Event source: AWS Events or EventBridge partner events -> Sample event type: AWS events -> Sample events: object created</h3>
<p align="left">
  <img src="screenshots/21.png" width="1000" height="600"/>
</p>
<h3>Creation method: use pattern form -> Event source: AWS services -> AWS service: s3 -> Event type: Amazon s3 event notification -> Specific events -> Object created -> Specific bucket name -> dataeng-clean-zone -> Next</h3>
<p align="left">
  <img src="screenshots/22.png" width="1000" height="600"/>
</p>
<h3>Target type: AWS service -> Select target: step function state machine -> State machine: ProcessFilesStateMachine -> Next</h3>
<p align="left">
  <img src="screenshots/23.png" width="1000" height="600"/>
</p>

<h3>Rules -> click the rule we just created -> click Edit pattern under Event pattern JSON</h3>
<p align="left">
  <img src="screenshots/24.png" width="1000" height="600"/>
</p>
<h3>modify JSON as below -> Next -> Update rule</h3>
<p align="left">
  <img src="screenshots/25.png" width="1000" height="600"/>
</p>

<h2>Testing our event driven data orchestration pipeline</h2>
<h3>Amazon S3 -> dataeng-clean-zone -> Create folder -> name: chapter10 as we provided on Eventbridge JSON rule -> Create folder</h3>
<p align="left">
  <img src="screenshots/26.png" width="1000" height="600"/>
</p>
<h3>move into chapter10 folder -> upload .csv file ->go to AWS Step Functions -> click on ProcessFilesStateMachinr -> from the list of execution you will see whether state machine Succeeded or Failed</h3>
<p align="left">
  <img src="screenshots/27.png" width="1000" height="600"/>
</p>










