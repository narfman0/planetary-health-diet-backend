import warnings

from flask_security import login_required

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask import Blueprint


blueprint = Blueprint("web", __name__)


@blueprint.route("/")
@login_required
def home():
    return "You are logged in!"
