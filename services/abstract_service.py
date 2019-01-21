from flask import Response
from mysql.db import sql_driver
from flask import jsonify, json
from services.errorHandler import ErrorHandler

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
        # res = Response(err_msg, status=status_code)
        if status_code is SUCCESS:

            res = jsonify(err_msg)
        else:
            res = Response(status=status_code)
        return res

    def return_validation_err(self, err):
        raise ErrorHandler(VALIDATION_ERR, err)

    def return_not_found(self, err):
        raise ErrorHandler(NOT_FOUND, err)

    def return_success(self, msg):
        return self.return_response(SUCCESS, msg)

    def return_internal_err(self, msg):
        raise ErrorHandler(ERROR, msg)
