class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

# _cats_count is a class variable that is incremented each time a Cat object is initialized.
# It is publicly accessible with the cats_count class method.
print(Cat.cats_count()) # 0
Cat("siamese")
print(Cat.cats_count()) # 1
for i in range(0, 5):
    Cat("siamese")
print(Cat.cats_count()) # 6
