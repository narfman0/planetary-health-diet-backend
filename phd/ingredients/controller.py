from phd import db


def list_ingredients(user_id):
    return db.get_entities("ingredients", "user_id", user_id)
