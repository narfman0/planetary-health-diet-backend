from flask_restplus import Namespace

api = Namespace(
    "meals", description="Meal definitions, containing one or more recipes and servings"
)
