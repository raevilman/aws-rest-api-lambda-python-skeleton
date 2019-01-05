import logging

# Setup logging
log_format = '%(asctime)s [%(filename)s:%(lineno)s - %(funcName)s()] [%(levelname)s] %(message)s'
logging.basicConfig(format=log_format)
logger = logging.getLogger("lambda-python")
logger.setLevel(logging.INFO)


class Function:
    @staticmethod
    def respond(status_code, res, req):
        return {
            'statusCode': status_code,
            'body': res,
            'context': req,
            'headers': {
                'Content-Type': 'application/json',
            }
        }

    @staticmethod
    def get_error_body(msg):
        return {
            'error': msg
        }

    @staticmethod
    def run(event, context):
        logger.info("In function.run")
        logger.info('Checking info if passed')
        if 'name' not in event:
            error_msg = 'name is a mandatory field for this operation'
            logger.error(error_msg)
            return Function.respond(status_code=400, res=Function.get_error_body(error_msg), req=event)
        elif 'greet_msg' not in event:
            error_msg = 'greet_msg is a mandatory field for this operation'
            logger.error(error_msg)
            return Function.respond(status_code=400, res=Function.get_error_body(error_msg), req=event)
        else:
            name = event['name']
            greet_msg = event['greet_msg']

            # Return the response
            response = {
                'show_msg': greet_msg + ", " + name
            }
            logger.info("Response")
            logger.info(response)
            return Function.respond(status_code=200, res=response, req=event)
