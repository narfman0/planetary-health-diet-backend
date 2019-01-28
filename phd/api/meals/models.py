from flask_restplus import fields

from phd.api.meals.api import api

meal_serving = api.model(
    "Meal portion",
    {
        "id": fields.Integer("Recipe ID", example=1),
        "servings": fields.Float("Number of servings from recipe"),
    },
)

meal = api.model(
    "Meal",
    {
        "portions": fields.List(fields.Nested(meal_serving)),
        "date": fields.DateTime(
            definition="Time of meal",
            dt_format="iso8601",
            example="2019-01-01T19:00:00Z",
        ),
    },
)
