# Get a salesperson's sales and commission rate.

# sales = float(input("Enter the amount of sales: "))
# comm_rate = float(input("Enter commission rate:"))
#
# Calculate the commission
# commission = sales * comm_rate
#
# Display the commission
# print("The commission is $" + format(commission))
#
# Get another salesperson's sales.....
# sales = float(input("Enter the amount of sales: "))
# comm_rate = float(input("Enter commission rate:"))
#
# Calculate the commission
# commission = sales * comm_rate
#
# Display the commission
# print("The commission is $" + format(commission))

# command + /

while True:
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter commission rate:"))

    commission = sales * comm_rate

    print("The commission is $" + format(commission))

    question = input("Do you want to keep calculating?").lower()

    if question == 'y' or question == 'yes':
        continue
    else:
        print("GoodBye!")
        break
