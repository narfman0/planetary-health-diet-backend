# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from flask import Flask, render_template

from phd.api import api


def create_app():
    app = Flask(__name__.split(".")[0])
    register_blueprints(app)
    register_errorhandlers(app)
    return app


def register_blueprints(app):
    app.register_blueprint(api.blueprint, url_prefix="/api/v1")


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
