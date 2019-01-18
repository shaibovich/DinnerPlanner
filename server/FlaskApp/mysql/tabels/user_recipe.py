from FlaskApp.services.errorHandler import ErrorHandler

TABLE_NAME = 'User_recipe'
DISH_TABLE = 'Dish'


def insert(user_id, dish_id, recipe):
    query = 'INSERT INTO {table} VALUES({dish_id},{user_id},"{recipe}")'.format(table=TABLE_NAME,
                                                                              user_id=user_id,
                                                                              dish_id=dish_id,
                                                                              recipe=recipe)
    return query


def get_all_user_recipes(user_id):
    query = 'SELECT * FROM {table}, {DISH_TABLE} WHERE {table}.user_id = {user_id} AND {table}.dish_id = {DISH_TABLE}.dish_id'.format(
        table=TABLE_NAME,
        DISH_TABLE=DISH_TABLE,
        user_id=user_id)
    return query
