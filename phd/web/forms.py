from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired


class CreateIngredientForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    food_group = SelectField("Food Group", coerce=int, validators=[DataRequired()])
