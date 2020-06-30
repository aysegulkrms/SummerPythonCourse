# While Loop

# Example

x = 0

# while x < 10:
#     print('x is currently :', x)
#     print('x is still less than 10, adding 1 to x')
#     x = x + 1
# else:
#     print("All done!")


# break, continue, pass
# break : breaks out of the loop
# continue: goes to the top of the closes enclosing loop
# pass: does nothing at all

while x < 10:
    print('x is currently :', x)
    print('x is still less than 10, adding 1 to x')
    x = x + 1  # x += 1
    if x == 3:
        print('x == 3')
        break
    else:
        print("continuing...")
        continue
print("******************\n")
# Program to add natural numbers up to n | sum = 1 + 2 + 3 + .... + n
# n will be entered by the user

number = int(input("Please enter a number: "))

add = 0
i = 1

while i <= number:
    add = add + i
    i = i + 1  # i += 1

print("The sum is =", add)
