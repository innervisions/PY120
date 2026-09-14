class Car:
    manufacturer = "Toyota"
    
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer
        
    def show_manufacturer(self):
        print(self.__class__.manufacturer)
        print(self.manufacturer)
        
car = Car("Ford")
car.show_manufacturer()
