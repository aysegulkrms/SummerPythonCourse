# Addition of Elements in a List

# Creating List
list_1 = []
print("Initial empty List:", list_1)

# Adding elements in the list
list_1.append(10)
list_1.append(35)
list_1.append(87)
print("\nList after adding three numbers", list_1)

# \n is creating a new line

# insert function
box = ["TV"]
box.insert(1, "Bicycle")
box.insert(2, "xbox")
print(box)

# Insert a macBook at index 0
box.insert(0, "macBook")
print(box)

# Extend Function
list_2 = [1, 2, 3, 4, 5, 6, 7]
print(list_2)
list_2.extend([8, 9, 10])
print(list_2)

# Updating Elements in List
box_2 = ["Fish", "Cat", "Dog"]
print("Before returning my cat", box_2)
box_2[1] = "Bird"
print("After returning my cat and buying a bird", box_2)

# Deleting Elements
del box_2[2]
print(box_2)

ch_list = ['A', 'F', 'Z', 'C', 'O']
ch_list.remove('Z')
print(ch_list)

# Deleting 2nd element
ch_list.pop(1)
print(ch_list)

# Deleting all elements
ch_list.clear()
print(ch_list)

# Challenge
list_3 = [23, 24, ["BMW", "Ford", "Toyota", "Honda"], [1999, 2000, 2001]]
# Please remove "Ford"
# Insert 2002 in the year list
print(len(list_3))
# list_3[2].remove('Ford')
# list_3[2].pop(1)
del list_3[2][1]
print(list_3)

# list_3[3].append(2002)
# list_3[3].insert(3, 2002)
list_3[3].extend([2002])
print(list_3)
