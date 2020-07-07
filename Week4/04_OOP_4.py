class Dog:
    # Class Attribute
    species = "mammal"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def speak(self, sound):
        print("{} says {}".format(self.name, sound))

    # Create an information function that prints Dog classes name and age
    def information(self):
        return "{} is {} years old".format(self.name, self.age)


philo = Dog("Philo", 6)
mikey = Dog("Mikey", 5)

philo.speak("Woof Woof")
print(philo.information())

print(mikey.information())

if philo.species == "mammal":
    print("{} is a {}!".format(philo.name, philo.species))
