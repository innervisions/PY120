class Bird:
    def __init__(self, species):
        self.species = species
        
class Sparrow(Bird):
    def __init__(self):
        super().__init__("sparrow")
        
bird = Sparrow()
print(bird.species)
