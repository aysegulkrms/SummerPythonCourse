import random

# Number Guessing game
# Randomly generate a number between 1-99
# if the user guesses a number that is lower than the generated number
# The program should say "guess higher"
# if the user guesses a number that is higher than the generated number
# the program should say "guess lower"
# if the user guesses the correct number the program should say you guessed it!

random_number = random.randint(1, 99)

while True:
    user_number = int(input("Please enter a number: "))
    if user_number == random_number:
        print("Congrats you guessed it!\nThe number was", random_number)
        break
    elif user_number > random_number:
        print("Guess lower")
    else:
        print("Guess higher")

