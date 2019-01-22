from flask import Flask, render_template, request
from mysql.db import sql_driver
from utils.utils import validate_request, validate_get_request
from services.user_service import user_service as user_services
from services.meal_service import meal_service as meal_services
from services.dish_service import dish_service as dish_services
from services.ingridents_service import ingridents_service as ingridents_services
from services.user_recipe_service import user_recipe_service as user_recipe_services
from services.errorHandler import ErrorHandler

app = Flask(__name__)
my_sql_driver = sql_driver(app)

# HERE PLEASE ADD CONSTRUCTOR FOR SERVICES
user_service = user_services(my_sql_driver)
meal_service = meal_services(my_sql_driver)
dish_service = dish_services(my_sql_driver)
ingridents_service = ingridents_services(my_sql_driver)
user_recipe_service = user_recipe_services(my_sql_driver)


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
    validate_get_request(request, ['user_id'])
    return meal_service.get_user_meals(request.args.get('user_id'))


@app.route('/deleteMeal', methods=['DELETE'])
def delete_user_meal():
    validate_get_request(request, ['user_id', 'meal_id'])
    meal_id = request.args.get('meal_id')
    user_id = request.args.get('user_id')
    return meal_service.delete_user_meal(meal_id, user_id)


#####################
#    INGREDIENTS    #
#####################

@app.route('/getIngredients', methods=['GET'])
def get_all_ing():
    if request.args and request.args.get('name'):
        return ingridents_service.search_ing(request.args.get('name'))
    else:
        return ingridents_service.get_all_ingridents()


@app.route('/addIngredient', methods=['POST'])
def add_ing():
    validate_request(request)
    return ingridents_service.add_ingrident(request.json)




#####################
#       Dishes      #
#####################
@app.route('/addDish', methods=['POST'])
def add_dish():
    validate_request(request)
    return dish_service.add_dish(request.json)


@app.route('/addEditRecipe', methods=['PUT'])
def edit_recipe():
    validate_request(request)
    return user_recipe_service.add_or_update_dish(request.json)


@app.route('/deleteRecipe', methods=['DELETE'])
def delete_user_recipe():
    validate_get_request(request, ['user_id', 'dish_id'])
    user_id = request.args.get('user_id')
    dish_id = request.args.get('dish_id')
    return user_recipe_service.delete_dish_recipe(user_id, dish_id)


@app.route('/searchDish', methods=['POST'])
def search_dishes():
    validate_request(request)
    return dish_service.search_dish(request.json)


@app.route('/getMyRecipes', methods=['GET'])
def search_user_recipes():
    validate_get_request(request, ['user_id'])
    return meal_service.get_user_edited_dishes(request.args.get('user_id'))


@app.route('/importDish', methods=['POST'])
def import_dishes():
    validate_request(request)
    return dish_service.import_dishes(request.json)

@app.errorhandler(ErrorHandler)
def all_exception_handler(error):
    return error.return_response()


if __name__ == "__main__":
    app.run(debug=True)
