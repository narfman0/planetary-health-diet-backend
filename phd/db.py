import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from google.cloud import datastore

from phd import log

logger = log.create_logger(__name__)


def get_entities(namespace, kind, key, value):
    entities = []
    query = datastore.Client(namespace=namespace).query(kind=kind)
    query.add_filter(key, "=", value)
    for item in query.fetch():
        item_id = item.get(key, None)
        if item_id is None:
            continue
        if item_id == value:
            entities.append(dict(item))
    return entities


def get_entity(namespace, kind, key, value):
    query = datastore.Client(namespace=namespace).query(kind=kind)
    query.add_filter(key, "=", value)
    for item in query.fetch():
        item_id = item.get(key, None)
        if item_id is None:
            continue
        if item_id == value:
            return dict(item)
