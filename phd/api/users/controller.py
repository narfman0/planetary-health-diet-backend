from phd import db


def get_user(user_id):
    return db.get_entity("users", "id", user_id)
