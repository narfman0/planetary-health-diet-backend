from flask_restplus import fields

from phd.api.recipes.api import api

recipe_ingredient = api.model(
    "Recipe ingredient",
    {
        "id": fields.Integer("Recipe ID", example=1),
        "amount": fields.Float("Quantity of ingredient used (in grams)", example=25.3),
    },
)

recipe = api.model(
    "Recipe",
    {
        "id": fields.Integer(description="Id of recipe", example=13),
        "name": fields.String(description="Name of recipe", example="Calzone"),
        "ingredients": fields.List(fields.Nested(recipe_ingredient)),
        "servings": fields.Integer(
            description="Number of servings recipe provides", example=4, default=1
        ),
        "calories_per_serving": fields.Integer(
            description="Number of calories per serving", example=200
        ),
    },
)
