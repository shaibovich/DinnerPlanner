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
        query = user_meal.insert(meal['user'], meal['name'])
        my_meal = self.db.insert(query)
        if 'dinnerList' in meal and len(list(meal['dinnerList'])):
            query = meal_dishes.insert_many(my_meal, meal['dinnerList'])
            query_res = self.db.insert(query)
            return self.return_success(meal)

    def search_meal(self, meal):
        query = user_meal.get(meal)
        if query:
            result = self.db.get(query)
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
