# Homework

# A software company sells package that retails for $99
# Quantity discounts are given below

# Quantity      Discount
# 10-19           10%
# 20-49           20%
# 50-99           30%
# 100 or more     40%

# Write a program that asks the user to enter the number of packages bought
# The program should display the amount of the discount(if any)
# The program should also display the total amount of the purchase after the discount


packages = int(input("Please enter the number of packages: "))
price = 99

if packages < 10:
    discount = 0
elif packages < 20:
    discount = 0.1
elif packages < 50:
    discount = 0.2
elif packages < 100:
    discount = 0.3
else:
    discount = 0.4

sub_total = price * packages
discount_amount = discount * sub_total
total = sub_total - discount_amount

print("Total is", total)
