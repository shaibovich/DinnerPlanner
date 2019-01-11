from FlaskApp.services.abstract_service import abstrac_service


class meal_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)

    def add_meal(self, meal):
        return self.return_internal_err("not implemented")  # TODO: implement
