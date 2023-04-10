from time import time, ctime


class Book:
    def __init__(self, name: str):
        if name is None or len(name) == 0:
            raise ValueError('no name given.')
        self.name = name
        self.creation_date = time()
        self.last_update = self.creation_date
        self.recipes_list = {}

    def __str__(self):
        """Return the string to print with the book info"""
        return f"""The book name is '{self.name}'
it was created on {ctime(self.creation_date)}
it was last updated on {ctime(self.last_update)}"""

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the \
                instance"""
        # ... Your code here ...

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        # ... Your code here ...

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        # ... Your code here ...
