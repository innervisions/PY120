class Person:
    def __init__(self, name):
        self.name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        
        self._name = name

guy = Person("Raymond")
print(guy.name)
guy.name = "Michael"
print(guy.name)
guy.name = 2        # raises TypeError
print(guy.name)
