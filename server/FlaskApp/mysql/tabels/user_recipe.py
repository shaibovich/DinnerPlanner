from FlaskApp.services.errorHandler import ErrorHandler

TABLE_NAME = 'User_recipe'
DISH_TABLE = 'Dish'


def insert(obj):
    validate_insert_obj(obj)
    query = 'INSERT INTO {table} VALUE({user_id}, {dish_id}, {calories}, "{recipe}", {peopleCount}, {cookingTime},"{photoLink}")'.format(
        table=TABLE_NAME,
        user_id=obj['user'],
        dish_id=obj['dish_id'],
        calories=obj['calories'],
        recipe=obj['recipe'],
        peopleCount=obj['peopleCount'],
        cookingTime=obj['cookingTime'],
        photoLink=obj['photoLink'])
    return query


def get_all_user_recipes(user_id):
    query = 'SELECT {DISH_TABLE}.dish_id, {DISH_TABLE}.name, {DISH_TABLE}.calories, {table}.recipe, {DISH_TABLE}.peopleCount, {DISH_TABLE}.cookingTime, {DISH_TABLE}.photoLink FROM {table}, {DISH_TABLE} WHERE {table}.user_id = {user_id} AND {table}.dish_id = {DISH_TABLE}.dish_id'.format(
        table=TABLE_NAME,
        DISH_TABLE=DISH_TABLE,
        user_id=user_id)
    return query


def get_user_recipe(user_id, dish_id):
    query = 'SELECT * FROM {table} WHERE user_id={user_id} AND dish_id={dish_id}'.format(table=TABLE_NAME,
                                                                                         user_id=user_id,
                                                                                         dish_id=dish_id)
    return query


def update_recipe(obj):
    validate_insert_obj(obj)
    query = 'UPDATE {table} SET calories={calories}, recipe="{recipe}", peopleCount={peopleCount}, cookingTime={cookingTime}, photoLink="{photoLink}" WHERE dish_id={dish_id} AND user_id={user_id}'.format(
        table=TABLE_NAME,
        calories=obj['calories'],
        recipe=obj['recipe'],
        peopleCount=obj['peopleCount'],
        cookingTime=obj['cookingTime'],
        photoLink=obj['photoLink'],
        dish_id=obj['dish_id'],
        user_id=obj['user']
    )
    return query


def validate_insert_obj(obj):
    if 'user' not in obj:
        raise ErrorHandler(403, "validation failed")
    if 'dish_id' not in obj:
        raise ErrorHandler(403, "validation failed")
    if 'calories' not in obj:
        raise ErrorHandler(403, "validation failed")
    if 'recipe' not in obj:
        raise ErrorHandler(403, "validation failed")
    if 'peopleCount' not in obj:
        raise ErrorHandler(403, "validation failed")
    if 'cookingTime' not in obj:
        raise ErrorHandler(403, "validation failed")
    if 'photoLink' not in obj:
        raise ErrorHandler(403, "validation failed")
