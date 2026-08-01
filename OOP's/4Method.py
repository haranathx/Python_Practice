# Methods are functions inside a class.

class Car:

    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(self.brand, "is starting")

car1 = Car("BMW")
car1.start()