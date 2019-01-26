from flask_restplus import Resource

from phd.api.users import controller, models
from phd.api.users.api import api

parser = api.parser()
parser.add_argument("userID", type=int)


@api.param("userID", "ID representing user")
@api.route("/<int:userID>/")
class UsersGet(Resource):
    @api.doc("get_user")
    @api.marshal_with(models.user)
    def get(self, userID):
        return controller.get_user(userID)


@api.route("/")
class UsersList(Resource):
    @api.doc("list_users")
    @api.marshal_list_with(models.user)
    def get(self):
        return controller.list_users()
