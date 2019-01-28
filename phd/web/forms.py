from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired


class CreateIngredientForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    food_group = SelectField("Food Group", coerce=int, validators=[DataRequired()])


class CreateRecipeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    servings = IntegerField("Servings", validators=[DataRequired()])
    calories_per_serving = IntegerField("Calories per serving")
    ingredients = TextAreaField(
        "Ingredient/Amount (in grams)", validators=[DataRequired()]
    )
