class SpeedMixin:
    def go_fast(self):
        print(f"I am a super fast {self.__class__.__name__}!")


class Car(SpeedMixin):
    def go_slow(self):
        print("I am safe and driving slow.")


small_car = Car()
small_car.go_fast()
# I am a super fast Car!

# self refers to the calling object which is an instance of the Car class.
# Thus self.__class__.__name__ is Car.
