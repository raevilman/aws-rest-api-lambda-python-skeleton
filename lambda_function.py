import json

from app.app import run
from app.event import Event
from app.responder import send_server_error
from app.utils import get_logger

# Setup logging
logger = get_logger("lambda_function")


def lambda_handler(request, context):
    logger.info('Request is ' + json.dumps(request))
    event = Event(event=request)
    try:
        return run(event)
    except Exception as e:
        import traceback
        info = traceback.format_exc()
        logger.error(info)
        return send_server_error(event.req_id())
