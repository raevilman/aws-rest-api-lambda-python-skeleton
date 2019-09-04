import logging
import json
from app.function import proxy_run

# Setup logging
log_format = '%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s()] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format)
logger = logging.getLogger("lambda_function")
logger.setLevel(logging.INFO)


def return_error(error_json):
    response = {
        'isBase64Encoded': 'false',
        'statusCode': '500',
        'body': json.dumps(error_json),
        'headers': {
            'Content-Type': 'application/json',
        }
    }
    logger.info("Sending response:" + json.dumps(response))
    return response


def lambda_handler(event, context):
    logger.info("In main.handler")
    try:
        # return run(event, context)
        return proxy_run(event, context)
    except Exception as e:
        import traceback
        info = traceback.format_exc()
        logging.error(info)
        error = {
            'error': "Something went wrong",
            'req_id': context.aws_request_id
        }
        return return_error(error)


if __name__ == '__main__':
    _body = {
            # 'greet_msg': 'Good day!',
            'name': 'John'
        }
    proxy_event = {
        'body': json.dumps(_body)
    }
    non_proxy_event = {
        # 'greet_msg': 'Good day!',
        'name': 'John'
    }
    _context = type("", (), dict(aws_request_id="dummy_aws_request_id"))()
    # lambda_handler(non_proxy_event, _context)
    lambda_handler(proxy_event, _context)
