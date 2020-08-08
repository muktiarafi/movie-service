class CustomError(Exception):
    def __init__(self, message, status_code, error):
        self.message = message
        self.status_code = status_code
        self.error = error

    def to_dict(self):
        rv = dict()
        rv['statusCode'] = self.status_code
        rv['message'] = self.message
        rv['error'] = self.error
        return rv
