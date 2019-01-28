from flask_wtf import FlaskForm
from wtforms import DateTimeField, IntegerField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired


class CreateIngredientForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    food_group = SelectField("Food Group", coerce=int, validators=[DataRequired()])


class CreateRecipeForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    servings = IntegerField("Servings", validators=[DataRequired()])
    calories_per_serving = IntegerField("Calories per serving")
    ingredients = TextAreaField(
        "Ingredient/Amount (in grams), newline delimtied", validators=[DataRequired()]
    )


class CreateMealForm(FlaskForm):
    date = DateTimeField("Date", validators=[DataRequired()])
    servings = TextAreaField(
        "Recipe/servings (newline delimited)", validators=[DataRequired()]
    )
