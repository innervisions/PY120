class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

dog = Dog("Poodle")
dog._breed = "Great Dane"
print(dog.get_breed())
