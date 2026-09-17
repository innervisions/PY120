class Fruit:
    def __init__(self, name):
        my_name = name


class Pizza:
    def __init__(self, name):
        self.my_name = name

# Only Pizza initializes an instance variable, as Fruit doesn't initialize a variable
# prefixed by self.

print(vars(Fruit("orange")))  # {}
print(vars(Pizza("pepperoni")))  # {'my_name': 'pepperoni'}
