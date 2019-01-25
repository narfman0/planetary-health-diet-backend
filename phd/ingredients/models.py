from flask_restplus import fields

from phd.ingredients.api import api

ingredient = api.model(
    "Ingredient",
    {
        "id": fields.Integer,
        "name": fields.String(description="Name of ingredient", example="Cheese"),
        "food_group_id": fields.Integer(
            description="ID of food group ingredient belongs in", example=7
        ),
    },
)
