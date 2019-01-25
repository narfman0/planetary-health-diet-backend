from phd import db


def list_recipes(user_id):
    return db.get_entities("recipes", "user_id", user_id)
