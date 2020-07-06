# Creating class Things
class Things:
    pass


# Creating Inanimate class
class Inanimate(Things):
    pass


# Creating Animate class
class Animate(Things):
    pass


# Creating Sidewalks Class
class Sidewalks(Inanimate):
    pass


# Creating Animals Class
class Animals(Animate):

    def eat(self):
        print("Eating")

    def breath(self):
        print("Breathing")

    def move(self):
        print("Moving")


# Creating Mammals Class
class Mammals(Animals):

    def feeding(self):
        print("Mammals feed their young with milk")


# Creating Giraffes Class
class Giraffes(Mammals):

    def eat_leaves(self):
        print("Giraffe is eating from the tree")


# Create 2 more classes that can inherit from Mammals
class Cats(Mammals):
    pass


class Dolphins(Mammals):
    pass


harold = Giraffes()

harold.move()
harold.feeding()
harold.breath()

reginald = Giraffes()
reginald.move()
