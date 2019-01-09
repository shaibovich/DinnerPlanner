from flaskext.mysql import MySQL
from FlaskApp.databaseUtil.utils import create_insert_query, create_select_query


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

    def insert(self, table, params):
        query = create_insert_query(table, params)
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except Exception:
            print("INSERT : error received from sql for query {query}".format(query=query))
            return False

    def select(self, tables, fields, conditions):
        query = create_select_query(tables, fields, conditions)
        try:
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            return result
        except Exception:
            print("SELECT : error received from sql for query {query}".format(query=query))
            return None
