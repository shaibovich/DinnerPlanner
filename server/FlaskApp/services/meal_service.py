from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.services.dish_service import dish_service as dish_services
from FlaskApp.mysql.tabels import meal_dishes
from FlaskApp.mysql.tabels import user_meal


## TODO check
class meal_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)
        self.dish_service = dish_services(my_sql)

    def add_meal(self, meal):
        query = user_meal.insert(meal['user'])
        if query and self.db.insert(query):
            my_meal = self.db.get(user_meal.get(meal['user']))[0][0]
            if len(list(meal['dishes'])):
                query = meal_dishes.insert(my_meal, meal['dishes'])
                if self.db.insert(query):
                    return self.return_success(meal)
                else:
                    return self.return_internal_err("db error for query : {}".format(query))

            return self.return_success(meal)
        else:
            return self.return_internal_err("db error fro query : {}".format(query))

    def search_meal(self, meal):
        query = user_meal.get(meal)
        if query:
            result = self.db.get(query)
            if result is None:
                self.return_internal_err("error")
            else:
                return self.return_success(self.convert_result_to_obj(result))
        return self.return_internal_err("error")

    def convert_result_to_obj(self, result):
        lst = []
        for res in result:
            lst.append({
                'id': res[0],
                'name': res[1],
                'dish': res[2],
                'date': res[3],
            })
        return lst
