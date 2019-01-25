from flask_restplus import Resource

from phd.recipes import controller, models
from phd.recipes.api import api

parser = api.parser()
parser.add_argument("userID", type=int)


@api.param("userID", "ID representing user to grab recipes for")
@api.route("/user/<int:userID>/")
class RecipeList(Resource):
    @api.doc("list_user_recipes")
    @api.marshal_list_with(models.recipe)
    def get(self, userID):
        return controller.list_recipes(userID)
