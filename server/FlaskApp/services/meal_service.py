from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.services.dish_service import dish_service as dish_services
from FlaskApp.services.ingridents_service import ingridents_service as ingridents_services
from FlaskApp.mysql.tabels import meal_dishes
from FlaskApp.mysql.tabels import user_meal


class meal_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)
        self.dish_service = dish_services(my_sql)
        self.ing_service = ingridents_services(my_sql)

    def add_meal(self, meal):
        query = user_meal.insert(meal['user'], meal['name'])
        my_meal = self.db.insert(query)
        if 'dinnerList' in meal and len(list(meal['dinnerList'])):
            # query = user_recipe.insert(meal['user'], id, dish['recipe'])
            # self.db.insert(query)
            query = meal_dishes.insert_many(my_meal, meal['dinnerList'])

            self.db.insert(query)
            return self.return_success(meal)

    def get_user_meals(self, user_id):
        query = user_meal.get(user_id)
        result = self.convert_result_to_obj(self.db.get(query))
        if result and len(result):
            for res in result:
                lst = []
                dish_query = meal_dishes.get_dishes(res['meal_id'])
                dish_query = meal_dishes.add_edited_dishes(user_id, dish_query)
                dish_lst = self.convert_dish(self.db.get(dish_query))
                for dish in dish_lst:
                    dish_ing_list = self.ing_service.get_all_dish_ingerients(dish['id'])
                    if dish_ing_list:
                        dish['ingredients'] = dish_ing_list
                    lst.append(dish)
                res['foods'] = lst

        return self.return_success(result)

    def get_user_edited_dishes(self, user_id):
        user_dishes = []
        query = user_meal.get(user_id)
        result = self.convert_result_to_obj(self.db.get(query))
        if result and len(result):
            for meal in result:
                dish_query = meal_dishes.get_dishes(meal['meal_id'])
                dish_query = meal_dishes.add_edited_dishes(user_id, dish_query)
                dish_lst = self.convert_dish(self.db.get(dish_query))
                for dish in dish_lst:
                    dish_ing_list = self.ing_service.get_all_dish_ingerients(dish['id'])
                    if dish_ing_list:
                        dish['ingredients'] = dish_ing_list
                    user_dishes.append(dish)
        return self.return_success(user_dishes)



    def delete_user_meal(self, meal_id, user_id):
        query = meal_dishes.delete_all_meal_dishes(meal_id)
        self.db.delete(query)
        query = user_meal.remove_meal(user_id, meal_id)
        self.db.delete(query)
        return self.return_success("success")



    def convert_dish(self, result):
        lst = []
        for res in result:
            lst.append({
                'id': res[0],
                'name': res[1],
                'calories': res[2],
                'recipe': res[3],
                'peopleCount': res[4],
                'cookingTime': res[5],
                'photoLink': res[6]
            })
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
