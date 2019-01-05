import logging
from app.function import Function

# Setup logging
log_format = '%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s()] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format)
logger = logging.getLogger("lambda-python")
logger.setLevel(logging.INFO)


def return_error(msg, req_id):
    return {
        'statusCode': '500',
        'body': {
            'error': msg
        },
        'context': {
            'req_id': req_id
        },
        'headers': {
            'Content-Type': 'application/json',
        }
    }


def lambda_handler(event, context):
    logger.info("In main.handler")
    try:
        response = Function.run(event, context)
        logger.info("Returning response")
        logger.info(response)
        return response
    except Exception as e:
        import traceback
        info = traceback.format_exc()
        logging.error(info)
        return return_error("Something went wrong", context.aws_request_id)


if __name__ == '__main__':
    event = {
        # 'greet_msg': 'Good day!',
        'name': 'John'
    }
    context = {}
    lambda_handler(event, context)
