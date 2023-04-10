recipe_types = ["starter", "lunch", "dessert"]


class Recipe():
    def __init__(self, name: str, cooking_lvl: int,
                 cooking_time: int, ingredients: list,
                 description: str, recipe_type: str):
        # check name
        if name is None or len(name) == 0:
            raise ValueError('no name given.')
        self.name = name
        # check cooking_lvl
        try:
            self.cooking_lvl = int(cooking_lvl)
        except ValueError:
            raise ValueError('cooking level Value Error, must be a number!')
        if self.cooking_lvl < 1 or self.cooking_lvl > 5:
            raise ValueError('cooking_lvl must be between 1 and 5.')
        # check cooking_time
        try:
            self.cooking_time = int(cooking_time)
        except ValueError:
            raise ValueError('cooking time Value Error, must be a number!')
        if self.cooking_time < 0:
            raise ValueError('cooking_time must be positive.')
        # check ingredients
        if type(ingredients) != list:
            raise ValueError('ingredients is not a list.')
        if len(ingredients) == 0:
            raise ValueError('ingredients is an empty list.')
        if any(type(ingre) is not str for ingre in ingredients):
            raise ValueError('ingredients have non string ingredients.')
        if any(ingre.strip() == '' for ingre in ingredients):
            raise ValueError('ingredients have empty ingredient.')
        # TODO: strip ingredients
        # check recipe_type
        if type(recipe_type) is not str:
            raise ValueError('recipe_type is not str.')
        if recipe_type not in recipe_types:
            # TODO: raise error !
            print("NOOOP!!!!")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"the string is {self.name}"
        return txt
