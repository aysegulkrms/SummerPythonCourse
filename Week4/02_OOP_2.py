# Naming the class usually starts with UpperCase
# OOP = Object Oriented Programming
class Dog:

    # Create the object right away
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return "Dog is eating"

    def bark(self):
        print("Dog is barking")


d = Dog("Tim", 5)
d.bark()
print(d.name)

string = d.eat()

print(type(d))


f = Dog("Milo", 4)
print(f.name)
print(f.age)
print(d.age)

print(type(f))
