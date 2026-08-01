# Used to give data when an object is created.


class Car:

    def __init__(self, brand, color):
        self.brand = brand           #self means this object.
        self.color = color

car1 = Car("BMW", "Black")

print(car1.brand)
print(car1.color)