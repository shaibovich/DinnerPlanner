from services.abstract_service import abstrac_service
from services.dish_service import dish_service as dish_services
from services.ingridents_service import ingridents_service as ingridents_services
from mysql.tabels import meal_dishes
from mysql.tabels import user_meal, dish_ingridents


class meal_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)
        self.dish_service = dish_services(my_sql)
        self.ing_service = ingridents_services(my_sql)

    def add_meal(self, meal):
        query, params = user_meal.insert(meal['user'], meal['name'])
        my_meal = self.db.insert(query, params)
        if 'dinnerList' in meal and len(list(meal['dinnerList'])):
            query, params = meal_dishes.insert_many(my_meal, meal['dinnerList'])
            self.db.insert(query, params)
            return self.return_success(meal)

    def get_user_meals(self, user_id):
        query, params = user_meal.get(user_id)
        result = self.convert_result_to_obj(self.db.get(query, params))
        if result and len(result):
            for res in result:
                lst = []
                dish_query, params = meal_dishes.get_dishes(res['meal_id'])
                dish_query = meal_dishes.add_edited_dishes(user_id, res['meal_id'], dish_query)
                dish_lst = self.convert_dish(self.db.get(dish_query, params))
                for dish in dish_lst:
                    dish_ing_list = self.ing_service.get_all_dish_ingerients(dish['id'])
                    if dish_ing_list:
                        dish['ingredients'] = dish_ing_list
                    lst.append(dish)
                res['foods'] = lst
                query, params = dish_ingridents.meal_ingredients(res['meal_id'])
                meal_ing = self.convert_meal_ing(self.db.get(query, params))
                res['ingList'] = meal_ing

        return self.return_success(result)

    def get_user_edited_dishes(self, user_id):
        query, params = meal_dishes.get_distinct_dishes(user_id)
        result = self.convert_dish(self.db.get(query, params), True)
        return self.return_success(result)

    def delete_user_meal(self, meal_id, user_id):
        query, params = meal_dishes.delete_all_meal_dishes(meal_id)
        self.db.delete(query, params)
        query, params = user_meal.remove_meal(user_id, meal_id)
        self.db.delete(query, params)
        return self.return_success("success")

    def convert_dish(self, result, with_meal=False):
        lst = []
        for res in result:
            obj = {
                'id': res[0],
                'name': res[1],
                'calories': res[2],
                'recipe': res[3],
                'peopleCount': res[4],
                'cookingTime': res[5],
                'photoLink': res[6]
            }
            if with_meal:
                obj['withMeal'] = res[7]
            lst.append(obj)
        return lst

    def convert_result_to_obj(self, result):
        lst = []
        for res in result:
            lst.append({
                'user_id': res[0],
                'meal_id': int(res[1]),
                'meal': res[2],
                'creation_date': res[3],
            })
        return lst

    def convert_meal_ing(self, result):
        lst = []
        for res in result:
            lst.append({
                'ing_id': res[1],
                'name': int(res[2]),
                'sum': res[3]
            })
        return lst
