import warnings

from flask import redirect, render_template, request
from flask_security import login_required
import flask_login

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask import Blueprint

from phd import db
from phd.api.food_groups.controller import FOOD_GROUPS as food_groups


blueprint = Blueprint("web", __name__)


@blueprint.route("/")
@login_required
def index():
    ingredients = db.get_entities("ingredient", "user_id", flask_login.current_user.id)
    return render_template("index.html", ingredients=ingredients)


@blueprint.route("/create/ingredient/", methods=["GET", "POST"])
@login_required
def create_ingredient():
    if request.method == "POST":
        item = dict(
            food_group_id=request.form["foodGroup"],
            name=request.form["name"],
            user_id=flask_login.current_user.id,
        )
        db.put_entity("ingredient", item)
        return redirect("/")
    else:
        return render_template("create_ingredient.html", food_groups=food_groups)
