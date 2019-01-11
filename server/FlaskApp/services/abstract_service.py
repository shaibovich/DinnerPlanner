from flask import Response
from FlaskApp.mysql.db import sql_driver

NOT_FOUND = 404
SUCCESS = 200
VALIDATION_ERR = 403
ERROR = 500


class abstrac_service:
    def __init__(self, db):
        if not isinstance(db, sql_driver):
            raise Exception("NO VALID SQL_DRIVER")
        self.db = db

    def return_response(self, status_code, err_msg):
        return Response(err_msg, status=status_code)

    def return_validation_err(self, err):
        return self.return_response(VALIDATION_ERR, err)

    def return_not_found(self, err):
        return self.return_response(NOT_FOUND, err)

    def return_success(self, msg):
        return self.return_response(SUCCESS, msg)

    def return_internal_err(self, msg):
        return self.return_response(ERROR, msg)
