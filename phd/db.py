import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from google.cloud import datastore

from phd import log

logger = log.create_logger(__name__)


def get_entities(kind, key=None, value=None):
    query = datastore.Client().query(kind=kind)
    if key and value:
        query.add_filter(key, "=", value)
    return [dict(item) for item in query.fetch()]


def get_entity(kind, key, value):
    return (get_entities(kind, key, value) or [None])[0]
