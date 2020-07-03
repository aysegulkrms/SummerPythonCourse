def adder(x, y, z):
    print("Sum:", x + y + z)


adder(10, 12, 13)


# Python *args
# Non Keyword Arguments

# Get numbers and add them all. Print the sum

def adder(*args):
    sum_num = 0
    for i in args:
        sum_num = sum_num + i
    print("The addition is:", sum_num)


adder(10, 20, 30, 40, 60)

# 1- Write a program that asks the user to enter a distance in kilometers
# 2- Write a function(def) that converts the kilometers to miles
# Miles = Kilometers * 0.6214
kilometers = int(input("Enter Kilometers"))


def km_to_miles(km):
    miles = km * 0.6214
    print(km, "is", format(miles, '0.1f'), 'miles')


km_to_miles(kilometers)
