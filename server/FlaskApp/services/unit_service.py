from FlaskApp.services.abstract_service import abstrac_service
from FlaskApp.mysql.tabels.unit import insert, get_all, exits


class unit_service(abstrac_service):
    def __init__(self, my_sql):
        abstrac_service.__init__(self, my_sql)

    def add_unit(self, unit):
        obj = self.validate_and_convert_ing(unit)
        if obj is None:
            return self.return_validation_err("Unit is invalid : {}".format(unit))
        query = insert(unit)
        if self.db.insert(query):
            return self.return_success(unit)
        else:
            return self.return_internal_err("db error for query : {}".format(query))

    def get_all_units(self):
        query = get_all()
        result = self.db.get(query)
        if result:
            return self.return_success(self.units_response(result))
        else:
            return self.return_internal_err("db error for query : {}".format(query))


    def validate_and_convert_ing(self, unit):
        if 'unit_type' not in unit:
            return None
        return (0, unit['unit_type'])

    def units_response(self, result_lst):
        list = []
        for res in result_lst:
            list.append({
                'id':res[0],
                'unit_type':res[1]
            })
        return list
