### Skeleton project for AWS Lambda - Python

Supports both proxy and non-proxy lambda from API Gateway  



| File name | Purpose |
| :---     |  :---
| lambda_function.py | Entry point for the lambda |  
| env.json | Environment variable of lambda when deployed (Not tested)  
| manage.py | Includes functions to package, create, deploy the lambda  
| app | Main source folder for the app. Logic should go in function.py -> run method or make changes accordingly.

#### _For non-proxy lambda_
Request body comes directly as event parameter

#### _For proxy lambda_

AWS article on ['Input format of a Lambda function for Proxy Integration'](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format)

```
Request JSON format for proxy integration
{
	"resource": "Resource path",
	"path": "Path parameter",
	"httpMethod": "Incoming request's method name"
	"headers": {Incoming request headers}
	"queryStringParameters": {query string parameters }
	"pathParameters":  {path parameters}
	"stageVariables": {Applicable stage variables}
	"requestContext": {Request context, including authorizer-returned key-value pairs}
	"body": "A JSON string of the request payload."
	"isBase64Encoded": "A boolean flag to indicate if the applicable request payload is Base64-encode"
}
Response JSON format
{
	"isBase64Encoded": true|false,
	"statusCode": httpStatusCode,
	"headers": { "headerName": "headerValue", ... },
	"body": "..."
}
```

#### _Test event for deployed lambda_
```
{
    "body": "{\"name\": \"John\"}"
}
```
**NOTE:**   
1. In manage.py, boto3 related functionality isn't tested, as I was exporting the zip only.  
2. Change the lib folder path in manage.py. Currently set to venv folder of pycharm.  