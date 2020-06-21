parrot = "Norwegian Blue"

# index method is used to retrieve the index number of a character in a string
print(parrot.index("n"))
print(parrot[:9])

# index(the letter to find, search starting index, search ending index)
print(parrot.index("e"))

print(parrot[10:])

print()
# Challenge : print "we win" on different lines using slices from the variable parrot
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
# Challenge : print "we win" on different lines using negative indexes
print(parrot[-11])  # w
print(parrot[-1])  # e
print(parrot[-5])  #
print(parrot[-11])  # w
print(parrot[-8])  # i
print(parrot[-6])  # n

# variable[start : stop : step]
name = "Silicone Labs"
print(name[0:8:3])

text = "Paris is the capital of France"
# print the letters by using a step number of 2
print(text[::2])  # If i don't type a starting index, it will start from 0
print(text[0::2])
print(text[0:30:2])

# len(variable) it will return the size of the text
print(len(text))
print(len("Python"))
print(len(parrot))

# Manual way to find the negative index
print(text.index("s") - len(text))
print(text[-30])
print(text[-26])

# Challenge : Print the numbers only!
title = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H, 9:I"
print(title[::5])
print(title[0::5])
print(title[0:-1:5])
print(title.index("1") - len(title))
print(title[-43::5])

# Challenge : Print the letters only!
print(title[2::5])
print(title[-41::5])