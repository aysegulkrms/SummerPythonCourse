# A company is giving a bonus of 5% to their employees if the employee served more than 5 years.
# Ask the user for their salary and year of service and print the salary with bonus(if they have bonus)
# 5 % = .05

# years = int(input("Please enter your years of service: "))
# salary = int(input("Please enter your salary: "))
#
# if years > 5:
#     salary *= 1.05
#     print("Your salary is", salary)
# else:
#     print("No bonus, salary is the same")


# Write a program to print absolute value of a number entered by the user
# INPUT:  1         OUTPUT : 1
# INPUT: -1         OUTPUT : 1

# 1st Solution
number = int(input("Please enter a number "))
# if number < 0:
#     number = -number
# print(number)

# 2nd Solution
number = abs(number)
print(number)
