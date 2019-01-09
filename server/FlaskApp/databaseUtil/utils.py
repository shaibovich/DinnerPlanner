def create_insert_query(table, params):
    params = params.values()
    query = 'INSERT INTO {table} VALUES('.format(table=table)
    for param in params:
        if isinstance(param, (int, float)):
            query += '{value},'.format(value=param)
        elif isinstance(param, str):
            query += '"{value}",'.format(value=param)
    query = query[:-1]
    query += ')'
    return query


def create_select_query(tables, fields, conditions):
    query = 'SELECT '
    if fields is None:
        query += '* '
    else:
        for index, field in enumerate(fields):
            query += '{field}'.format(field=field)
            if index != len(fields)-1:
                query += ','

    query += 'FROM '
    for index, table in enumerate(tables):
        query += '{table}'.format(table=table)
        if index != len(tables)-1:
            query += ','
    query += ' WHERE '
    for index, condition in enumerate(conditions):
        first_var = condition[0]
        operator = condition[1]
        second_var = condition[2]
        query += "{first}{op}'{second}'".format(first=first_var, op=operator, second = second_var)
        if index != len(conditions)-1:
            query += ' AND '
    return query
