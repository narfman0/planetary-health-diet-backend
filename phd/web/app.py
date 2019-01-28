import warnings
from datetime import datetime

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


@blueprint.route("/")
@login_required
def index():
    ingredients = db.get_entities("ingredient", "user_id", flask_login.current_user.id)
    ingredient_map = {int(ingredient["id"]): ingredient for ingredient in ingredients}
    recipes = db.get_entities("recipe", "user_id", flask_login.current_user.id)
    recipe_map = {int(recipe["id"]): recipe for recipe in recipes}
    meals = db.get_entities("meal", "user_id", flask_login.current_user.id)
    for recipe in recipes:
        for ingredient in recipe["ingredients"]:
            ingredient["name"] = ingredient_map[int(ingredient["id"])]["name"]
    for meal in meals:
        for portion in meal["portions"]:
            portion["name"] = recipe_map[int(portion["id"])]["name"]
    return render_template(
        "index.html",
        food_groups=food_groups.list_food_groups(),
        ingredients=ingredients,
        recipes=recipes,
        meals=meals,
    )


@blueprint.route("/create/ingredient/", methods=["GET", "POST"])
@login_required
def create_ingredient():
    form = forms.CreateIngredientForm()
    form.food_group.choices = [
        (fg.id, fg.name) for fg in food_groups.list_food_groups()
    ]
    if form.validate_on_submit():
        item = dict(
            food_group_id=int(form.data["food_group"]),
            name=form.data["name"],
            user_id=flask_login.current_user.id,
        )
        db.put_entity("ingredient", item)
        return redirect("/")
    return render_template(
        "create_ingredient.html", food_groups=food_groups.list_food_groups(), form=form
    )


@blueprint.route("/create/recipe/", methods=["GET", "POST"])
@login_required
def create_recipe():
    form = forms.CreateRecipeForm()
    if form.validate_on_submit():
        ingredients = []
        for line in form.data["ingredients"].splitlines():
            ingredient, amount = line.rsplit(" ", 1)
            ingredient_candidate = db.get_entity("ingredient", "name", ingredient)
            if ingredient_candidate:
                ingredient = ingredient_candidate["id"]
            else:
                raise Exception(f"No ingredient found with name {ingredient}")
            amount = float(amount)
            ingredients.append(dict(id=ingredient, amount=amount))
        item = dict(
            name=form.data["name"],
            servings=form.data["servings"],
            calories_per_serving=form.data.get("calories_per_serving", None),
            ingredients=ingredients,
            user_id=flask_login.current_user.id,
        )
        db.put_entity("recipe", item)
        return redirect("/")
    return render_template("create_recipe.html", form=form)


@blueprint.route("/create/meal/", methods=["GET", "POST"])
@login_required
def create_meal():
    form = forms.CreateMealForm()
    form.date.data = datetime.utcnow()
    if form.validate_on_submit():
        portions = []
        for line in form.data["servings"].splitlines():
            recipe, servings = line.rsplit(" ", 1)
            recipe_candidate = db.get_entity("recipe", "name", recipe)
            if recipe_candidate:
                recipe = recipe_candidate["id"]
            else:
                raise Exception(f"No recipe found with name {recipe}")
            servings = float(servings)
            portions.append(dict(id=recipe, servings=servings))
        item = dict(
            date=form.data["date"].isoformat(),
            portions=portions,
            user_id=flask_login.current_user.id,
        )
        db.put_entity("meal", item)
        return redirect("/")
    return render_template("create_meal.html", form=form)
