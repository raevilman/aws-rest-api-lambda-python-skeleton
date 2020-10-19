import json


def send_response(status: int, body: str):
    response = {
        "statusCode": status,
        "body": body
    }
    return response


def send_ok_response(body: str):
    return send_response(200, body)


def send_server_error(req_id: str):
    error = {
        'error': "Something went wrong",
        'req_id': req_id
    }
    return send_response(500, json.dumps(error))
