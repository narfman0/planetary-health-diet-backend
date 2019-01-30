from phd import settings

if settings.DB_ENGINE == "ndb":
    from phd.security.ndb import datastore, models

    user_datastore = datastore.NDBUserDatastore(models.User, models.Role)
else:
    from flask_security import SQLAlchemySessionUserDatastore
    from phd.security.sql import datastore, models

    user_datastore = SQLAlchemySessionUserDatastore(
        datastore.db_session, models.User, models.Role
    )
    datastore.init_db()
