#### Course prerequisites

    Lambda Deep Dive
    AWS Essentials
    Introduction to Python Development
    

##### Essentials

    Serverless means that you can run code
    without provisioning or managing server
    You pay only for the compute time you consume
    By default, Lambda is highly available, fault-torelant,scalable, elastic, and cost-efficient
    
    Lambda functions are the core concept when programming with Lambda, and consist of:
    Your application
    Any application dependencies your code requires, such as libraries, configurations, 
    or other resources.
    
    Lamda easily integrates with many other AWS services including:
    CloudWatch Logs for monitoring.
    API Gateway for exposing HTTP endpoints backed by Lambda
    KMS for working encryptation keys.
    Many other services through the AWS SDK and the IAM Role assigned
    to Lambda function on creation.
    
    Lambda supports Java,Go,Powershell,Nodejs.C#,Python and Ruby code, and provides a 
    Runtime API which allows you to use any additional programming languages.
    
    Lambda fuctions are triggered by events. These events may include:
    HTTP API request throuh API Gateway
    CloudWatch scheduled events
    S3 file uploads
    DynamoDB Streams changes.
    Direct Invocations using the CLI or SDK
    
    Lambda programming model:
    Handler files and functions the entry potin for Lambda invocations
    Events the incoming data passed to a Lambda function when
    triggered.
    COntext-provides methods and properties that provide information
    about the invocation, function and execution environment.
    Logging
    Exceptions success or failure in comuunicate to AWS
