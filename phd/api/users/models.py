from flask_restplus import fields

from phd.api.users.api import api

user = api.model(
    "User",
    {
        "id": fields.Integer(description="ID of user", example=1),
        "email": fields.String(description="Email of user", example="jim@example.com"),
    },
)
