def greet(name):
    """This function greets the person passed in as a parameter"""
    print("Hello", name, "Good Morning")


print(greet.__doc__)

print(len.__doc__)
print(abs.__doc__)

greet("James")


def absolute_value(num):
    """This function returns the absolute value of the entered number"""
    return abs(num)


print(absolute_value(-5))
print(absolute_value(3))


def my_func():
    x = 10
    print("Value inside function:", x)


# We can't access a variable that is created inside the function
# print(x) x is not defined
x = 20
my_func()
print("Value outside function:", x)


# A simple Python function to check if a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


even_odd(5)
even_odd(10)


# *args entering multiple parameters(arguments)

def my_func_2(*args):
    for i in args:
        print(i, end=" ")


my_func_2("Hello", "Welcome", "to", "Python", "class")
print()

# Create a function that would take multiple number of arguments *args
# Greet people with first name and last name
first_name = input("First name: ")
last_name = input("Last name: ")


def greeting(*args):
    print("Hello", end=" ")
    for i in args:
        print(i, end=" ")


greeting(first_name, last_name)
