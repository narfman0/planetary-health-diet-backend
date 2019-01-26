import os

DB_ENGINE = os.environ.get("PHD_DB_ENGINE", "sqlite")
DB_HOSTNAME = os.environ.get("PHD_DB_HOSTNAME", "phd-host")
DB_USERNAME = os.environ.get("PHD_DB_USERNAME", "phd_user")
DB_PASSWORD = os.environ["PHD_DB_PASSWORD"]
DB_NAME = os.environ.get("PHD_DB_NAME", "phd")
PASSWORD_SALT = os.environ["PHD_PASSWORD_SALT"]
SECRET_KEY = os.environ["PHD_SECRET_KEY"]
