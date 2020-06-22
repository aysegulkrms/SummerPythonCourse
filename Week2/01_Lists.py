# Lists can contain DataTypes like Integers, Strings and many more...

# Create A List []
list_1 = []
print("Blank List", list_1)
print(type(list_1))

# Creating a List of Numbers
list_2 = [10, 20, 25]
print("\nList of Numbers", list_2)

# Creating a List of Strings and Accessing using index numbers
programming_languages = ["Java", "C++", "Python", "Javascript", "SQL"]
print("Index number 1", programming_languages[1])
print("Index number 2", programming_languages[2])

# Creating a Multi-Dimensional List(By Nesting a List inside a List)
shopping_list = [["Apples", "Bananas", "Strawberries"], ["Milk", "Cheese"]]
print("\nShopping List:", shopping_list)
print(shopping_list[1])
print(shopping_list[1][1])
print(shopping_list[0][1])
print(shopping_list[0][2])

# Creating a list with the use of Numbers(Having Duplicate Values)
list_3 = [1, 2, 4, 4, 4, 3, 3, 6, 2]
print("\nList with Numbers", list_3)

# Creating a List with mixed type of values(Having numbers and Strings)
list_4 = [1, 4, 50, "Gorilla", "Bear", "Lion", 2.5]
print("\nList with mixed types", list_4)
print(len(list_4))
