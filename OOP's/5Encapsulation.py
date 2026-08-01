# Keep data inside a class.

class Employee:

    def __init__(self, name):
        self.name = name

emp = Employee("Rahul")

print(emp.name)