class Cat:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() == other.name.casefold()
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        return self.name.casefold() != other.name.casefold()
    
cat1 = Cat("Yoshi")
cat2 = Cat("Al")
cat3 = Cat("Yoshi")

print(cat1 == cat2) # False
print(cat1 != cat2) # True
print(cat1 == cat3) # True
print(cat1 != cat3) # False
print(cat1 == "Yoshi") # False
