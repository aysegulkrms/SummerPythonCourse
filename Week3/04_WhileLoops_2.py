import random
# Write a program to ask if user wants to roll the dice
# If yes then roll the dice and print it. Ask if they want to roll it again
# Keep on asking until they say no

# question = input("Would you like to roll the dice? (Y/N) ").lower()

# while question == "yes" or question == 'y':
#     i = random.randint(1, 6)
#     print(i)
#     question = input("Would you like to roll the dice again? ").lower()
# else:
#     print("Dice game ended...")

# answer = random.choice(['Yes', 'No', 'Okay'])
# print(answer)

# Challenge
# Ask for a min value of the dice
# Ask for a max value of the dice

min_value = int(input("Enter the minimum value of the dice: "))
max_value = int(input("Enter the maximum value of the dice: "))

while True:
    print(random.randint(min_value, max_value))
    another_roll = input("Roll again? (Y/N)").lower()
    if another_roll == "y" or another_roll == "yes":
        continue
    else:
        print("Dice game ended...")
        break

