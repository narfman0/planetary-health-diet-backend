import warnings

from flask import redirect, render_template
from flask_security import login_required
import flask_login

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask import Blueprint

from phd import db
from phd.models import food_groups
from phd.web import forms


blueprint = Blueprint("web", __name__)


def food_group_choices():
    return [(fg.id, fg.name) for fg in food_groups.list_food_groups()]


@blueprint.route("/")
@login_required
def index():
    ingredients = db.get_entities("ingredient", "user_id", flask_login.current_user.id)
    return render_template("index.html", ingredients=ingredients)


@blueprint.route("/create/ingredient/", methods=["GET", "POST"])
@login_required
def create_ingredient():
    form = forms.CreateIngredientForm()
    form.food_group.choices = food_group_choices()
    if form.validate_on_submit():
        item = dict(
            food_group_id=form.data["food_group"],
            name=form.data["name"],
            user_id=flask_login.current_user.id,
        )
        db.put_entity("ingredient", item)
        return redirect("/")
    return render_template(
        "create_ingredient.html", food_groups=food_groups.list_food_groups(), form=form
    )
