
class Forest:
    height = 100
    weight = 5
    age = 25
    color_list = 'green'
    breed = "Dub"

    def __int__(self):
        print(Forest.height)
        print(Forest.age)

tree1 = Forest()
print(tree1)

class Student:
    group = "c2013"
    def __init__(self, age, name=None , hight=160):
        self.weight = 50
        self.hight = 150
        self.age = age
        self.name = name

    def printer(self):
        print(self.weight)

    def grow(self, hight=10):
        self.hight += hight

    def __str__(self):
        return f"I'm student. My name is {self.name} and i'm {self.age} years old."

nick = Student(15, "Nick", 150)
kate = Student(16, "kate", 140)
print(nick)
print(kate)
print(nick.age)
print(kate.age)
print(nick.hight)
print(kate.hight)
kate.grow()
print(kate.hight)
kate.grow(25)
print(kate.hight)