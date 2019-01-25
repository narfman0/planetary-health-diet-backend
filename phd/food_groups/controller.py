class FoodGroup:
    def __init__(self, name, grams):
        self.name = name
        self.grams = grams


FOOD_GROUPS = [
    FoodGroup("Beef, lamb, pork protein", 14.0),
    FoodGroup("Added sugars", 31.0),
    FoodGroup("Starchy vegetables", 50.0),
    FoodGroup("Added fats", 51.8),
    FoodGroup("Poultry, eggs, seafood, plant protein", 195.0),
    FoodGroup("Fruits", 200.0),
    FoodGroup("Whole grains", 232.0),
    FoodGroup("Dairy", 250.0),
    FoodGroup("Vegetables", 300.0),
]

total_grams = sum([food_group.grams for food_group in FOOD_GROUPS])
for food_group in FOOD_GROUPS:
    food_group.ratio = food_group.grams / total_grams


def list_food_groups():
    return FOOD_GROUPS
