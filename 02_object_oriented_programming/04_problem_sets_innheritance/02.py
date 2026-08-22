class Pet:
    def speak():
        pass

    def run(self):
        return "running!"

    def jump(self):
        return "jumping!"

    def sleep(self):
        return "sleeping!"


class Dog(Pet):
    def speak(self):
        return "bark!"

    def fetch(self):
        return "fetching!"


class Bulldog(Dog):
    def sleep(self):
        return "snoring!"


class Cat(Pet):
    def speak(self):
        return "meow!"

pet = Pet()
dave = Dog()
bud = Bulldog()
kitty = Cat()

print(pet.run())  # running!
print(kitty.run())  # running!
print(kitty.speak())  # meow!
try:
    kitty.fetch()
except Exception as exception:
    print(exception.__class__.__name__, exception, "\n")
    # AttributeError 'Cat' object has no attribute 'fetch'

print(dave.speak())  # bark!

print(bud.run())  # running!
print(bud.sleep())  # "snoring!"
