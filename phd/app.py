# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask import Flask, render_template
    from flask_security import Security

from phd import settings
from phd.api import api
from phd.web import app as web_app
from phd.security.datastore import user_datastore


def create_app():
    app = Flask(__name__.split(".")[0])
    app.config["SECRET_KEY"] = settings.SECRET_KEY
    app.config["SECURITY_PASSWORD_SALT"] = settings.PASSWORD_SALT
    app.config["SECURITY_REGISTERABLE"] = True
    app.config["SECURITY_SEND_REGISTER_EMAIL"] = False
    register_blueprints(app)
    register_errorhandlers(app)
    register_security(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api.blueprint, url_prefix="/api/v1")
    app.register_blueprint(web_app.blueprint, url_prefix="/")


def register_security(app):
    Security(app, user_datastore)


def register_errorhandlers(app):
    def render_error(error):
        """Render error template."""
        # If a HTTPException, pull the `code` attribute; default to 500
        error_code = getattr(error, "code", 500)
        return render_template("{0}.html".format(error_code)), error_code

    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None


if __name__ == "__main__":
    create_app()  # pragma: no cover
