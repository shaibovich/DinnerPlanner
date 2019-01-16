TABLE_NAME = "Ingridents"


def insert(ing):
    if not validate_object(ing):
        return False  # error
    # TODO possibly add {if !exits(ing)}
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
    query = 'SELECT * FROM {table} WHERE dish_id={dish_id}'.format(table=TABLE_NAME,
                                                                   dish_id=dish_id)
    return query


def validate_object(ing):
    if 'name' not in ing:
        return False
    return True
