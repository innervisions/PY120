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

print(Pet.mro())
print(Cat.mro())
print(Dog.mro())
print(Bulldog.mro())
