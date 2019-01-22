# -*- coding: utf-8 -*-

import MySQLdb

from services.errorHandler import ErrorHandler


class sql_driver:
    def __init__(self, app):
        self.mysql = MySQLdb.connect(
            host="localhost",
            user="DbMysql10",
            passwd="DbMysql10",
            db="DbMysql10"
        )
        self.conn = self.mysql
        self.cursor = None

    def insert(self, query, params):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(query, params)
            self.cursor.close()
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print("INSERT : error received from sql for query {query} with error {error}".format(query=query,
                                                                                                 error=e))

            if e.args[0] == 1062:
                raise ErrorHandler(400, "Already Exists")
            else:
                raise ErrorHandler(500, e)

    def is_exists(self, query, params):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            self.cursor.close()
            return len(result) > 0
        except Exception as e:
            print("SELECT : error received from sql for query {query}".format(query=query))
            raise ErrorHandler(500, e)

    def get(self, query, params):
        try:
            self.cursor = self.conn.cursor()
            if params == ():
                self.cursor.execute(query)
            else:
                self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            self.cursor.close()
            return result
        except Exception as e:
            print("SELECT : error received from sql for query {query} ׳with error {err}".format(query=query,
                                                                                                err=e))
            raise ErrorHandler(500, e)

    def delete(self, query, params):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(query, params)
            self.cursor.close()
            self.conn.commit()
            return True
        except Exception as e:
            print("DELETE : error received from sql for query {query}".format(query=query))
            raise ErrorHandler(500, e)
