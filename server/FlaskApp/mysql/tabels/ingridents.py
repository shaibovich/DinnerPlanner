from FlaskApp.services.errorHandler import ErrorHandler
TABLE_NAME = "Ingredients"


def insert(ing):
    if not validate_object(ing):
        raise ErrorHandler(403, "validation error")
    query = "INSERT INTO {table} VALUES(0, '{name}')".format(table=TABLE_NAME,
                                                             name=ing['name'])
    return query


def insert_many(ing_list):
    query = "INSERT INTO {table} (id,name) VALUES".format(table=TABLE_NAME)
    for index, ing in enumerate(ing_list):
        # TODO possibly add {if !exits(ing)}
        query += '(0, "{name}")'.format(name=ing['name'])
        if index != len(ing_list) - 1:
            query += ','
        else:
            query += ';'
    return query


def get_all():
    query = "SELECT * FROM {table}".format(table=TABLE_NAME)
    return query


def exists(ing):
    if not validate_object(ing):
        return False  # error
    query = 'SELECT COUNT(*) as count FROM {table} WHERE name="{name}"'.format(table=TABLE_NAME,
                                                                               name=ing['name'])
    return query


def get_by_dish_id(dish_id):
    query = 'SELECT I.ing_id, I.name, {table}.amount FROM {table}, Ingredients as I WHERE {table}.dish_id={dish_id} AND {table}.ing_id = I.ing_id'.format(
        table='Dish_ingredients',
        dish_id=dish_id)
    return query

def get_by_name(name):
    query = 'SELECT * FROM {table} where name="{name}"'.format(table=TABLE_NAME,
                                                             name=name)
    return query


def validate_object(ing):
    if 'name' not in ing:
        return False
    return True
