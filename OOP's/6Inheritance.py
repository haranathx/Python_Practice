# One class can reuse another class.

class Animal:

    def sound(self):
        print("Some sound")

class Dog(Animal):
    pass

dog = Dog()
dog.sound()