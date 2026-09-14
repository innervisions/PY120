class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return "Name not set!"


cat = Cat()
print(cat.get_name())  # Name not set!
