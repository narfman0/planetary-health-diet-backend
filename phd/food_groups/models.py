from flask_restplus import fields

from phd.food_groups.api import api

food_group = api.model(
    "Food Group",
    {
        "id": fields.Integer(description="ID for food group", example=7),
        "name": fields.String(description="Name of food group", example="Dairy"),
        "grams": fields.Float(description="Suggested gram intake daily", example=250.0),
        "ratio": fields.Float(description="Total ratio per day", example=0.18),
    },
)
