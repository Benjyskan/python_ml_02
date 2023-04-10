class Recipe:
    def __init__(self, name: str, cooking_lvl: int, cooking_time: int, ingredients: list, description: str, recipe_type: str):
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
        print(ingredients)
        # NOT WORKING
        if [type(ingre) is not str for ingre in ingredients]:
            raise ValueError('ingredients have non string ingredients.')

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"the string is {self.name}"
        return txt
