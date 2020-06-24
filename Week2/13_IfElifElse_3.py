# name = input("Enter a name: ")
#
# if name == "Max":
#     print("Name entered is :", name)
# elif name == "John":
#     print("Name entered is :", name)
# elif name == "Eli":
#     print("Name entered is :", name)
# else:
#     print("The name entered is invalid")


# Challenge:
# Ask the user for a time number(int) int(input("Enter a time"))
# if time is before 10 print "good morning"
# if time is after 10 and before 12 print "Soon time for a lunch"
# if time is after 12 and before 18 print "Good Day"
# if the time is after 18 and before 22 print "good evening"
# if the time is after 22 print "Good night"

time = int(input("Enter a time "))
if 0 <= time < 24:
    if time <= 10:
        print("Good Morning")
    elif 10 < time <= 12:
        print("Soon time for a lunch")
    elif 12 < time <= 18:
        print("Good Day")
    elif 18 < time < 22:
        print("Good evening")
    else:
        print("Good night")
else:
    print("This is not a correct time buddy")
