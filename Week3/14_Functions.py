# Functions in Python

# How To create a function
# def == defining function

def name_of_function():
    print("Hello")
    print("How are you?")


name_of_function()
name_of_function()


# Parameterized Function
def greeting(name, last_name):
    print("Hello", name, last_name)


greeting("Cemil", "Koc")


def add_numbers(num_1, num_2):
    print(num_1 + num_2)


add_numbers(5, 10)
add_numbers(10, 25)
add_numbers(50, 30)


# create a function to find the average of 2 numbers
def average(num_1, num_2):
    print((num_1 + num_2) / 2)


average(10, 16)


# Return for function
def add_num(num_1, num_2):
    return num_1 + num_2


result = add_num(5, 10)
print(result)

result_2 = add_num(6, 20)
print(result_2)


# Prime numbers
# prime numbers are numbers that can be divided to 1 and to itself
# 2, 3, 5, 7, 11, 13.....

def is_prime(num):
    for n in range(2, num):
        if num % n == 0:
            print(num, "is not a prime")
            break
        else:
            print(num, "is prime")
            break


is_prime(7)
is_prime(10)
is_prime(8)
