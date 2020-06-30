# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the addition
add = 0

# Iterate over the list
for i in numbers:
    add = add + i

print("The sum is", add)

# Program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz', 'classical']
print(len(genre))

for i in range(len(genre)):
    print("I like", genre[i])

# Example
# String
for letter in "This is a string":
    print(letter)

print()
# Tuple
tuple_1 = (1, 2, 3, 4, 5)
for t in tuple_1:
    print(t)

list_1 = [(2, 4, 14), (6, 8, 16), (10, 12, 18)]
for tup in list_1:
    print(tup)

# Unpacking
for t1, t2, t3 in list_1:
    print(t1, t2, t3)

# Dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}

# .keys(), .values(), .items()
print(d.items())
print(d.keys())
print(d.values())

for k, v in d.items():
    print(k, v)

for v in d.values():
    print(v)

print()
# for loop with else
digits = [1, 2, 5, 7]
for i in digits:
    print(i)
else:
    print("No more items left")

# Challenge!
# Create an empty list
# Using a for loop append even numbers from 0-41 to the empty list
# print out the list

list_2 = []
# 0, 2, 4..... 40

# First solution
# for i in range(0, 41):
#     if i % 2 == 0:
#         list_2.append(i)

print(list_2)

# Second Solution
for i in range(0, 41, 2):
    list_2.append(i)
print(list_2)

# Challenge!
# use the list from 0-41
# make a new list which will store square of elements of previous list

print()
list_3 = []

for i in list_2:
    list_3.append(i ** 2)

print(list_3)
