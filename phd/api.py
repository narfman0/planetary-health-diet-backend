import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask import Blueprint
    from flask_restplus import Api

from phd.food_groups import api as ns_food_groups


blueprint = Blueprint("api", __name__)
api = Api(blueprint)
api.add_namespace(ns_food_groups)
