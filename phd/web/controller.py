from phd import db
from phd.models import food_groups


def get_food_group_proportions(meals):
    """ Calculate the proportions from given meals """
    proportion_map = {food_group.id: 0 for food_group in food_groups.list_food_groups()}
    for meal in meals:
        for portion in meal["portions"]:
            consumed_servings = portion["servings"]
            recipe = db.get_entity("recipe", "id", portion["id"])
            recipe_servings = recipe["servings"]
            for recipe_ingredient in recipe["ingredients"]:
                ingredient_id = recipe_ingredient["id"]
                ingredient = db.get_entity("ingredient", "id", ingredient_id)
                food_group_id = ingredient["food_group_id"]
                current_group_grams = proportion_map[food_group_id]
                proportion_map[food_group_id] = (
                    current_group_grams
                    * recipe_ingredient["amount"]
                    * (consumed_servings / recipe_servings)
                )
    return proportion_map
