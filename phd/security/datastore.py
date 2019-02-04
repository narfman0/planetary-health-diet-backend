import warnings
from phd import settings


if settings.DB_ENGINE == "ndb":
    from phd.security.ndb import datastore, models

    user_datastore = datastore.NDBUserDatastore(models.User, models.Role)
elif settings.DB_ENGINE == "ds":
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        from google.cloud import datastore as gcp_ds
    from phd.security.ds import datastore, models

    user_datastore = datastore.DSUserDatastore(
        gcp_ds.Client(), models.User, models.Role
    )
else:
    from flask_security import SQLAlchemySessionUserDatastore
    from phd.security.sql import datastore, models

    user_datastore = SQLAlchemySessionUserDatastore(
        datastore.db_session, models.User, models.Role
    )
    datastore.init_db()
