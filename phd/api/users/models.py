from flask_restplus import fields

from phd.api.users.api import api

user = api.model(
    "User",
    {
        "id": fields.Integer(description="ID of user", example=1),
        "name": fields.String(description="Name of user", example="Steve"),
    },
)
