from flask import Flask, render_template, request
from FlaskApp.mysql.db import sql_driver
from FlaskApp.utils.utils import validate_request
from FlaskApp.services.user_service import user_service as user_services

app = Flask(__name__)
my_sql_driver = sql_driver(app)
user_service = user_services(my_sql_driver)


#####################
#       INDEX       #
#####################

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


#####################
#        USER       #
#####################


@app.route('/login', methods=['POST'])
def login():
    validate_request(request)
    return user_service.login(request.json)


@app.route('/signup', methods=['POST'])
def signup():
    validate_request(request)
    return user_service.signup(request.json)


if __name__ == "__main__":
    app.run(debug=True)
