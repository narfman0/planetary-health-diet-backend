from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from phd import settings

if settings.DB_ENGINE == "sqlite":
    engine = create_engine("sqlite:////tmp/phd.db", convert_unicode=True)
else:
    connection_string = (
        f"mysql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}"
        + f"@{settings.DB_HOSTNAME}/{settings.DB_NAME}"
    )
    engine = create_engine(connection_string, convert_unicode=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from phd.security import models  # noqa

    Base.metadata.create_all(bind=engine)
