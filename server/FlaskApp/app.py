from flask import Flask, render_template, request, Response
from FlaskApp.databaseUtil.databaseApi import sql_driver
from FlaskApp.utils.utils import validate_signup, validate_request, validate_login

app = Flask(__name__)
my_sql_driver = sql_driver(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    validate_request(request)
    validate_login(request.json)
    conditions = [
        ('email', '=', request.json['email']),
        ('password', '=', request.json['password'])
    ]
    if my_sql_driver.select(['User'], None, conditions):
        return Response("success", status=200)
    else:
        return Response("failed", status=404)


@app.route('/signup', methods=['POST'])
def signup():
    validate_request(request)
    validate_signup(request.json)
    if my_sql_driver.insert('User', request.json):
        return Response("success", status=200)
    else:
        return Response("fail", status=403)


# @app.route('/users')
# def users():
# cur=mysql.connection.cursor()
# resVal = cur.execute("SELECT * FROM User")
# if resVal > 0:
#     userDetails = cur.fetchall()
#     render_template('users.html', userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)
