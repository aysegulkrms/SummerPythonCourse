person = "Sammy"

if person == 'Sammy':
    print("Welcome Sammy!")
else:
    print("Who are you ?")

person_2 = 'Jimmy'

if person_2 == 'Sammy':
    print("Welcome Sammy")
elif person_2 == 'George':
    print('Welcome George')
else:
    print("What is your name?")

# ----------Nested IF Statements----------

person_3 = 'Sammy'
last_name = "Columbus"

if person_3 == 'Michael':
    if last_name == "Johnson":
        print("Welcome Michael Johnson")
    else:
        print("Michael, What is your last name?")
elif person_3 == 'Sammy':
    if last_name == "John":
        print("Welcome Sammy John")
    else:
        print("Sammy what is your last name?")
else:
    print("Who are you?")


# I will check if x is positive
# If x is positive I will also check if it even or odd number
# % modulo | x % 2 == 0 Even number check

x = 11

print(x % 2 == 0)

if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is negative")

print("*******************\n")

number = int(input("Please Enter a number: "))
if number >= 0:
    if number == 0:
        print("The number you entered is zero")
    else:
        print("Number is positive")
else:
    print("Negative number")


