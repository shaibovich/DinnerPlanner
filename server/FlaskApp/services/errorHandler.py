from flask import jsonify

NOT_FOUND = 404
SUCCESS = 200
VALIDATION_ERR = 403
ERROR = 500


class ErrorHandler(Exception):
    def __init__(self, status_code, msg):
        super().__init__(msg)
        self.status_code = status_code
        self.err = msg

    def return_response(self):
        response = jsonify({'err': self.err})
        response.status_code = self.status_code
        return response
