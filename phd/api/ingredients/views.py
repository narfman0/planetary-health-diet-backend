from flask_restplus import Resource

from phd.api.ingredients import controller, models
from phd.api.ingredients.api import api

parser = api.parser()
parser.add_argument("userID", type=int)


@api.param("userID", "ID representing user to grab ingredients for")
@api.route("/user/<int:userID>/")
class IngredientList(Resource):
    @api.doc("list_user_ingredients")
    @api.marshal_list_with(models.ingredient)
    def get(self, userID):
        return controller.list_ingredients(userID)
