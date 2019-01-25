from flask_restplus import Namespace

api = Namespace(
    "recipes", description="Recipe definitions with different amounts of ingredients"
)
