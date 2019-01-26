from phd.security.datastore import user_datastore


def get_user(user_id):
    return user_datastore.get_user(user_id)


def list_users():
    raise NotImplementedError
