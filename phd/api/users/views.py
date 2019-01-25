from flask_restplus import Resource

from phd.api.users import controller, models
from phd.api.users.api import api

parser = api.parser()
parser.add_argument("userID", type=int)


@api.param("userID", "ID representing user")
@api.route("/user/<int:userID>/")
class UserGet(Resource):
    @api.doc("get_user")
    @api.marshal_with(models.user)
    def get(self, userID):
        return controller.get_user(userID)
