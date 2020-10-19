import json

from app.event import Event
from app.responder import send_ok_response
from app.utils import get_logger

# Setup logging
logger = get_logger("app")


def run(event: Event):
    logger.info(event.http_path())
    logger.info(event.http_method())
    return send_ok_response(json.dumps({
        'message': 'Hello'
    }))
