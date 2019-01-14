TABLE_NAME = "Unit"


def insert(uni):
    if not validate_object(uni):
        return False  # error
    query = "INSERT INTO {table} VALUES(0, '{name}')".format(table=TABLE_NAME,
                                                             name=uni['unit_type'])
    return query


def get_all():
    query = "SELECT * FROM {table}".format(table=TABLE_NAME)
    return query


def exists(uni):
    if not validate_object(uni):
        return False  # error
    query = 'SELECT COUNT(*) as count FROM {table} WHERE unit_type="{unit_type}"'.format(table=TABLE_NAME,
                                                                                         unit_type=uni['unit_type'])
    return query


def validate_object(uni):
    if 'unit_type' not in uni:
        return False
    return True
