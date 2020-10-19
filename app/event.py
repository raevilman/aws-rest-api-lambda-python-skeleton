class Event:
    def __init__(self, event):
        self.event = event

    def req_context(self):
        return self.event['requestContext']

    def http_path(self):
        return self.event['path']

    def http_method(self):
        return self.event['httpMethod']

    def req_id(self):
        return self.req_context()['requestId']
