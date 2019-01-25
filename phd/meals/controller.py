from phd import db


def list_meals(user_id):
    return db.get_entities("meals", "user_id", user_id)
