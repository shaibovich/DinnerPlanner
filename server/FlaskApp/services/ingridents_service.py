from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels.ingridents import insert, get_all, exits, insert_many


class ingridents_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)

    def add_ingrident(self, ing):
        obj = self.validate_and_convert_ing(ing)
        if obj is None:
            return self.return_validation_err("Ing is invalid : {}".format(ing))
        query = insert(ing)
        if self.db.insert(query):
            return self.return_success(ing)
        else:
            return self.return_internal_err("db error for query : {}".format(query))

    def add_ingridents(self, ing_list):
        new_insert_list = []
        for ing in ing_list:
            obj = self.validate_and_convert_ing(ing_list[ing])
            if obj is None:
                return self.return_validation_err("validation failed")
            else:
                query = exits(ing_list[ing])
                if self.db.is_exists(query) is False:
                    new_insert_list.append(ing_list[ing])
        if len(new_insert_list) == 0:
            return None
        query = insert_many(new_insert_list)
        if self.db.insert(query):
            return self.return_success(new_insert_list)
        else:
            return self.return_internal_err("db error for query : {}".format(query))

    def get_all_ingridents(self):
        query = get_all()
        result = self.db.get(query)
        if result:
            return self.return_success(self.ingredients_response(result))
        else:
            return self.return_internal_err("db error for query : {}".format(query))



    def validate_and_convert_ing(self, ing):
        if 'name' not in ing:
            return None
        return (0, ing['name'])

    def ingredients_response(self, result_lst):
        list = []
        for res in result_lst:
            list.append({
                'id':res[0],
                'name':res[1]
            })
        return list
