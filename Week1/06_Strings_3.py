# The + operator concatenates strings. It returns a string consisting of the operands joined together

s = "Apple"
t = "iPhone"
u = "11 Pro"

print(s + " " + t)

# Without whitespace
print(s + t + u)

# With Whitespace
print(s + " " + t + " " + u)

print("Go TEAM" + "!!!")

# The * operator will print multiple copies of a string
name = 'cemil.'
print((name + " ") * 5)
print(name * 5)

# The number may be negative or zero. But they will return an empty string

print("name * -8" + (name * -8))
print(name * -8)

str_1 = 'Hello'
str_2 = 'World'
# Combine the strings and print them out
print(str_1 + " " + str_2)

str_3 = "Hello World"

str_3 = str_3 + ' concatenate me!'
print(str_3)

# Combining numbers with Strings
print("Addition:", (2 + 1))  # When combining numbers with string use a comma(,)

m = 'my name is Cemil'

# Upper() method
print(m.upper())

# lower() method
print(m.lower())

# Capitilize
print(m.capitalize())

# split : split a string by blank space
print(m.split())

# Split by a specific element
print(m.split("n"))
print(m.split("i"))

# .format()
print('Insert another string with curly brackets: {}'.format('The inserted string'))
print("My name is {}, and my last name is {} ".format("Cemil", "Koc"))

name = "Adam"
last_name = "Johnson"
print("His name is {} and his last name is {}".format(name, last_name))

# Placeholder method %s
print("I am going to inject %s here" % "something")
print("I am going to inject %s text here, and %s text here." % ('some', 'more'))

# print your name and last name using placeholder %s method
name_1 = "Cemil"
last_name_1 = "Koc"
print("My name is %s and my last name is %s" % (name_1, last_name_1))

print("Hello {}, your balance is {}.".format("Adam", 380.56))
print("Hello {0}, your balance is {1}.".format("Adam", 380))  # 0, 1
print("Hello {2}, your balance is {1}.".format("Adam", 380, "Johnson"))
print("Hello {name}, your balance is {balance}.".format(name='Johnson', balance=500))

# Padding and precision of floating point numbers
print("Floating point numbers: %0.5f" %(13.144490))



