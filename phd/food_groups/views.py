from flask_restplus import Resource

from phd.food_groups import controller, models
from phd.food_groups.api import api


@api.route("/")
class FoodGroupsList(Resource):
    @api.doc("list_food_groups")
    @api.marshal_list_with(models.food_group)
    def get(self):
        return controller.list_food_groups()
