from flask_security import SQLAlchemySessionUserDatastore

from phd.security.database import db_session, init_db
from phd.security.models import User, Role

user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
init_db()
