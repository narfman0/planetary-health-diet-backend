from flask_restplus import fields

from phd.meals.api import api

meal_serving = api.model(
    "Meal serving", {"recipe_id": fields.Integer, "servings": fields.Float}
)

meal = api.model(
    "Meal",
    {
        "servings": fields.List(fields.Nested(meal_serving)),
        "date": fields.DateTime(
            definition="Time of meal",
            dt_format="iso8601",
            example="2019-01-01T19:00:00Z",
        ),
    },
)
