from flask_restplus import fields

from phd.recipes.api import api

recipe_ingredient = api.model(
    "Recipe ingredient",
    {
        "ingredient_id": fields.Integer,
        "amount": fields.Float("Quantity of ingredient used (in grams)", example=25.3),
    },
)

recipe = api.model(
    "Recipe",
    {
        "id": fields.Integer(description="Id of recipe", example=13),
        "name": fields.String(description="Name of recipe", example="Calzone"),
        "ingredients": fields.List(fields.Nested(recipe_ingredient)),
    },
)
