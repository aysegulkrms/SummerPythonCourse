a = int(input("Enter your first number "))
b = int(input("Enter your second number "))

operation = input("Enter the first capital letter of the operation[A, S, M, D] ").upper()

if operation == "A":
    print("The addition of {} and {} is {}.".format(a, b, a + b))
elif operation == "S":
    print("The difference of {} and {} is {} ".format(a, b, a-b))
elif operation == "M":
    print("The multiplication of {} and {} is {}".format(a, b, a * b))
elif operation == "D":
    print("The division of {} and {} is {}".format(a, b, a / b))
else:
    print("Invalid operator")