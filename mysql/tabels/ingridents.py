from services.errorHandler import ErrorHandler

TABLE_NAME = "Ingredients"


def insert(ing):
    validate_object(ing)
    query = "INSERT INTO {table} VALUES(0, %s)".format(table=TABLE_NAME)
    return query, (ing['name'])


def insert_many(ing_list):
    query = "INSERT INTO {table} (id,name) VALUES".format(table=TABLE_NAME)
    values = ()
    for index, ing in enumerate(ing_list):
        validate_object(ing)
        query += '(0, %s)'
        values += (ing['name'])
        if index != len(ing_list) - 1:
            query += ','
        else:
            query += ';'
    return query, values


def get_all():
    query = "SELECT * FROM {table}".format(table=TABLE_NAME)
    return query, ()


def exists(ing):
    validate_object(ing)
    query = 'SELECT COUNT(*) as count FROM {table} WHERE name=%s'.format(table=TABLE_NAME)
    return query, ing['name']


def get_by_dish_id(dish_id):
    query = 'SELECT I.ing_id, I.name, {table}.amount FROM {table}, Ingredients as I WHERE {table}.dish_id=%s AND {table}.ing_id = I.ing_id'.format(
        table='Dish_ingredients')
    return query, (dish_id)


def get_by_name(name):
    query = 'SELECT * FROM {table} where name LIKE "{name}%"'.format(table=TABLE_NAME,
                                                                     name=name)
    return query, ()


def validate_object(ing):
    if 'name' not in ing:
        raise ErrorHandler(403, "Ingredient : validation failed, no ingredient name")
