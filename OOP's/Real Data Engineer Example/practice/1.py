class student:
    
    def __init__(self, name, age):
        self.name=name
        self.age=age


    def intro(self):
        print("hallo my name is", self.name)
        print(self.age, "years old")


stu1=student("Hara", 26)
stu2=student("Alax", 25)

stu1.intro()
stu2.intro()