
from flask import Flask, render_template, request, redirect, send_file, Response
from flask_mysqldb import MySQL

import os
# import yaml
app = Flask(__name__)


# config db
# db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = db['mysql_host']
# app.config['MYSQL_USER'] = db['mysql_user']
# app.config['MYSQL_PASSWORD'] = db['mysql_password']
# app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # fetch data
        userDetails = request.form
        name= userDetails['name']
        email= userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO User(name,email) VALUES (%s %s)",(name, email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    if (request.is_json):
        print(request.json)
        test = request.json['password']
        if test == '123456':
            return Response("test",status=200)
        else:
            return Response('invalid password', status=403)


@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    resVal = cur.execute("SELECT * FROM User")
    if resVal > 0:
        userDetails = cur.fetchall()
        render_template('users.html', userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)
