class Bird:
    def __init__(self, species):
        self.species = species


class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)       # Fix
        self.color = color


birdie = Sparrow("sparrow", "brown")
print(birdie.species)  # Will raise AttributeError without fix
