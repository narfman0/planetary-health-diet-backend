import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask import Blueprint
    from flask_restplus import Api

from phd.api.food_groups import api as ns_food_groups
from phd.api.ingredients import api as ns_ingredients
from phd.api.meals import api as ns_meals
from phd.api.recipes import api as ns_recipes
from phd.api.users import api as ns_users


blueprint = Blueprint("api", __name__)
api = Api(blueprint)
api.add_namespace(ns_food_groups)
api.add_namespace(ns_ingredients)
api.add_namespace(ns_meals)
api.add_namespace(ns_recipes)
api.add_namespace(ns_users)
