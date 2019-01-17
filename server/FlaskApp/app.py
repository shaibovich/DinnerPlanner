from flask import Flask, render_template, request
from FlaskApp.mysql.db import sql_driver
from FlaskApp.utils.utils import validate_request
from FlaskApp.services.user_service import user_service as user_services
from FlaskApp.services.meal_service import meal_service as meal_services
from FlaskApp.services.dish_service import dish_service as dish_services
from FlaskApp.services.ingridents_service import ingridents_service as ingridents_services
from FlaskApp.services.errorHandler import ErrorHandler
app = Flask(__name__)
my_sql_driver = sql_driver(app)

# HERE PLEASE ADD CONSTRUCTOR FOR SERVICES
user_service = user_services(my_sql_driver)
meal_service = meal_services(my_sql_driver)
dish_service = dish_services(my_sql_driver)
ingridents_service = ingridents_services(my_sql_driver)



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
    try:
        return user_service.signup(request.json)
    except ErrorHandler as e:
        return e.return_response()


# TODO: all from here

#####################
#     USER_MEAL     #
#####################
@app.route('/addMeal', methods=['POST'])
def add_meal():
    validate_request(request)
    return meal_service.add_meal(request.json)


@app.route('/getMyMeal', methods=['GET'])
def get_user_meals():
    validate_request(request)


@app.route('/editMeal', methods=['PUT'])
def edit_meal():
    validate_request(request)


#####################
#    INGREDIENTS    #
#####################
@app.route('/getIngredients', methods=['GET'])
def get_all_ing():
    validate_request(request)
    return ingridents_service.get_all_ingridents()


#####################
#       Dishes      #
#####################
@app.route('/addDish', methods=['POST'])
def add_dish():
    validate_request(request)
    return dish_service.add_dish(request.json)


@app.route('/editDish', methods=['PUT'])
def edit_dish():
    validate_request(request)


@app.route('/deleteDish', methods=['DELETE'])
def delete_dish():
    validate_request(request)


@app.route('/searchDish', methods=['POST'])
def search_dishes():
    validate_request(request)
    return dish_service.search_dish(request.json)


if __name__ == "__main__":
    app.run(debug=True)
