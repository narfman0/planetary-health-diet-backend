from flask_restplus import Resource

from phd.meals import controller, models
from phd.meals.api import api

parser = api.parser()
parser.add_argument("userID", type=int)


@api.param("userID", "ID representing user to grab meals for")
@api.route("/user/<int:userID>/")
class MealsList(Resource):
    @api.doc("list_user_meals")
    @api.marshal_list_with(models.meal)
    def get(self, userID):
        return controller.list_meals(userID)
