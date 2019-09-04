import logging
import json
from app.vars import APP_NAME

# Setup logging
log_format = '%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s()] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format)
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)

'''
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
'''

def respond(status_code, res):
    response = {
        'isBase64Encoded': 'false',
        'statusCode': status_code,
        'body': json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
    logger.info("Sending response:" + json.dumps(response))
    return response


def get_error_body(msg, req_id):
    return {
        'error': msg,
        'req_id': req_id
    }


def proxy_run(event, context):
    logger.info("In function.proxy_run")
    body = json.loads(event['body'])
    logger.info(body)
    logger.info('Checking info if passed')
    if 'name' not in body:
        error_msg = 'name is a mandatory field for this operation'
        logger.error(error_msg)
        return respond(status_code=400, res=get_error_body(error_msg, context.aws_request_id))
    elif 'greet_msg' not in body:
        error_msg = 'greet_msg is a mandatory field for this operation'
        logger.error(error_msg)
        return respond(status_code=400, res=get_error_body(error_msg, context.aws_request_id))
    else:
        name = body['name']
        greet_msg = body['greet_msg']

        # Return the response
        response = {
            'show_msg': greet_msg + ", " + name
        }
        return respond(status_code=200, res=response)


def run(event, context):
    logger.info("In function.run")
    logger.info('Checking info if passed')
    if 'name' not in event:
        error_msg = 'name is a mandatory field for this operation'
        logger.error(error_msg)
        return respond(status_code=400, res=get_error_body(error_msg, context.aws_request_id))
    elif 'greet_msg' not in event:
        error_msg = 'greet_msg is a mandatory field for this operation'
        logger.error(error_msg)
        return respond(status_code=400, res=get_error_body(error_msg, context.aws_request_id))
    else:
        name = event['name']
        greet_msg = event['greet_msg']

        # Return the response
        response = {
            'show_msg': greet_msg + ", " + name
        }
        logger.info("Response")
        logger.info(response)
        return respond(status_code=200, res=response)
