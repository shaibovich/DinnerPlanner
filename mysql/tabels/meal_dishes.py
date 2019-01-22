from services.errorHandler import ErrorHandler
import datetime

TABLE_NAME = 'Meal_dishes'


def insert(meal_id, dish_id):
    creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    validate_insert(meal_id, dish_id, creation_date)
    query = 'INSERT INTO {table} VALUES(%s, %s, %s)'.format(table=TABLE_NAME)
    return query, (meal_id, dish_id, creation_date)


def insert_many(meal_id, dish_list):
    query = 'INSERT INTO {table} (meal_id, dish_id) VALUES '.format(table=TABLE_NAME)
    values = ()
    for index, dish in enumerate(dish_list):
        query += '(%s, %s)'
        values += (meal_id, dish)
        if index == len(dish_list) - 1:
            query += ';'
        else:
            query += ','
    return query, values


def delete_all_meal_dishes(meal_id):
    query = 'DELETE FROM {table} WHERE meal_id=%s'.format(table=TABLE_NAME)

    return query, (meal_id)


def validate_insert(meal_id, dish_id, creation_date):
    if dish_id is None or meal_id is None or creation_date is None:
        raise ErrorHandler(403, "Meal Dishes : validation failed, must fill : meal_id(int) , dish_id(int)")


def validate_get(meal_id):
    if meal_id is None:
        raise ErrorHandler(403, "Meal Dishes : validation failed, must add meal_id(int)")


def get_dishes(meal_id):
    validate_get(meal_id)
    query = 'SELECT Dish.dish_id,  ' \
            'Dish.name, ' \
            'Dish.calories, ' \
            'Dish.recipe, ' \
            'Dish.peopleCount, ' \
            'Dish.cookingTime, ' \
            'Dish.photoLink ' \
            'FROM {table}, Dish  ' \
            'WHERE {table}.meal_id=%s ' \
            'AND {table}.dish_id = Dish.dish_id '.format(
        table=TABLE_NAME)
    return query, (meal_id)


def add_edited_dishes(user_id, meal_id, query):
    query = '(' + query + 'AND Dish.dish_id '
    query += 'NOT IN (SELECT dish_id FROM User_recipe WHERE user_id={user_id}))'.format(user_id=user_id)
    query += ' UNION '
    query += '(SELECT Dish.dish_id,' \
             ' Dish.name, ' \
             'User_recipe.calories, ' \
             'User_recipe.recipe, ' \
             'User_recipe.peopleCount, ' \
             'User_recipe.cookingTime, ' \
             'User_recipe.photoLink ' \
             'FROM User_recipe, Dish, {table} ' \
             'WHERE user_id={user_id} ' \
             'AND Dish.dish_id = User_recipe.dish_id ' \
             'AND {table}.meal_id = {meal_id} ' \
             'AND {table}.dish_id=Dish.dish_id)'.format(user_id=user_id, table=TABLE_NAME, meal_id=meal_id)
    return query


def get_distinct_dishes(user_id):
    query = ' (SELECT Dish.dish_id,' \
            ' Dish.name,' \
            ' Dish.calories,' \
            ' Dish.recipe,' \
            ' Dish.peopleCount,' \
            ' Dish.cookingTime,' \
            ' Dish.photoLink,' \
            ' 0 as fromMeal' \
            ' FROM Meal_dishes, Dish, (' \
            ' SELECT meal_id FROM User_meals WHERE user_id = %s) as meals' \
            ' WHERE Meal_dishes.dish_id = Dish.dish_id' \
            ' AND meals.meal_id = Meal_dishes.meal_id' \
            ' AND Dish.dish_id NOT IN' \
            ' (SELECT dish_id' \
            ' FROM User_recipe' \
            ' WHERE user_id=%s))' \
            ' UNION' \
            ' (SELECT Dish.dish_id,' \
            ' Dish.name,' \
            ' User_recipe.calories,' \
            ' User_recipe.recipe,' \
            ' User_recipe.peopleCount,' \
            ' User_recipe.cookingTime,' \
            ' User_recipe.photoLink,' \
            ' 1 as fromMeal' \
            ' FROM User_recipe, Dish , Meal_dishes,' \
            ' (SELECT meal_id FROM User_meals WHERE user_id = %s) as meals' \
            ' WHERE User_recipe.user_id=%s' \
            ' AND Dish.dish_id = User_recipe.dish_id' \
            ' AND Meal_dishes.meal_id = meals.meal_id' \
            ' AND Meal_dishes.dish_id = Dish.dish_id)'
    return query, (user_id, user_id, user_id, user_id)


def remove_dish_from_meal(meal_id, dish_id):
    validate_insert(meal_id, dish_id, None)

    query = 'DELETE FROM {table} WHERE(meal_id = %s AND dish_id = %s)'.format(table=TABLE_NAME)

    return query, (meal_id, dish_id)
