from flaskext.mysql import MySQL
from FlaskApp.services.errorHandler import ErrorHandler

class sql_driver:
    def __init__(self, app):
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = 'DbMysql10'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'DbMysql10'
        app.config['MYSQL_DATABASE_DB'] = 'DbMysql10'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        self.mysql.init_app(app)
        self.conn = self.mysql.connect()
        self.cursor = self.conn.cursor()

    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print("INSERT : error received from sql for query {query} with error {error}".format(query=query,
                                                                                                 error=e))
            raise ErrorHandler(500, e)

    def is_exists(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result[0][0] > 0
        except Exception as e:
            print("SELECT : error received from sql for query {query}".format(query=query))
            raise ErrorHandler(500, e)

    def get(self, query):
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print("SELECT : error received from sql for query {query} ׳with error {err}".format(query=query,
                                                                                                err=e))
            raise ErrorHandler(500, e)

    def delete(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except Exception as e:
            print("DELETE : error received from sql for query {query}".format(query=query))
            raise ErrorHandler(500, e)
