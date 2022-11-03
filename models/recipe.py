recipe_list = []


def get_last_id():
    if recipe_list:
        last_recipe = recipe_list[-1]
    else:
        return 1
    return last_recipe.id + 1


class Recipe:
    def __init__(self, name, ingredients, description, serving_size, cook_time, instructions, thumbnail):
        self.id = get_last_id()
        self.name = name
        self.ingredients = ingredients
        self.description = description
        self.thumbnail = thumbnail
        self.serving_size = serving_size
        self.cook_time = cook_time
        self.instructions = instructions
        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients,
            'description': self.description,
            'thumbnail': self.thumbnail,
            'serving_size': self.serving_size,
            'cook_time': self.cook_time,
            'instructions': self.instructions,
        }
