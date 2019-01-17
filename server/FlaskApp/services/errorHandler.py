from flask import Response
from flask import jsonify, json
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
        return Response(status=self.status_code)
