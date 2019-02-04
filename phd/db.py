import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from google.cloud import datastore


def delete_entity(kind, key):
    client = datastore.Client()
    key = client.key(kind, key)
    client.delete(key)


def get_entities(kind, key=None, value=None, filters=[]):
    query = datastore.Client().query(kind=kind)
    if key and value:
        query.add_filter(key, "=", value)
    for filter_key, filter_type, filter_value in filters:
        query.add_filter(filter_key, filter_type, filter_value)
    results = []
    for item in query.fetch():
        addition = dict(item)
        addition["id"] = int(item.id)
        results.append(addition)
    return results


def get_entity(kind, key, value):
    if key == "id":
        client = datastore.Client()
        entity_key = client.key(kind, value)
        return client.get(entity_key)
    return (get_entities(kind, key, value) or [None])[0]


def put_entity(kind, item):
    client = datastore.Client()
    key = client.key(kind)
    entity = datastore.Entity(key=key)
    entity.update(item)
    client.put(entity)
