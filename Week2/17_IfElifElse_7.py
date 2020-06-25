# Take two int values from user and print the greatest among them

# number_1 = int(input("Please enter the first number "))
# number_2 = int(input("Please enter the second number "))
#
# if number_1 > number_2:
#     print("Greatest is", number_1)
# elif number_2 > number_1:
#     print("Greatest is", number_2)
# else:
#     print("Both are equal")


# Ask user for quantity
# Suppose that an item will cost 100
# The shop will give discount of 10% if the cost of purchased quantity is more than 1000
# Calculate the total cost

quantity = int(input("Please enter a quantity"))
cost = quantity * 100

if cost > 1000:
    cost *= 0.9  # cost = cost * 0.9

print("Total cost is", cost)
