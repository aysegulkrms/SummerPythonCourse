# Range in python
list_1 = list(range(0, 11))
print(list_1)

list_2 = list(range(0, 11, 2))
print(list_2)

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

for i in range(5):
    print("Hello {}".format(i))

for i in range(11):
    print(i, end=" ")

print()
# modulo
print(17 % 5)

print(10 % 3)

print(18 % 7)

# Example
# Even numbers 2, 4, 6, 8, 10
# i % 2 == 0

for i in range(11):
    if i % 2 == 0:
        print(i, end=" ")

print("\n")
list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in list_3:
    print(i )

print()

for i in list_3:
    if i % 2 != 0:
        print(i)
    else:
        print("This is an even number")

