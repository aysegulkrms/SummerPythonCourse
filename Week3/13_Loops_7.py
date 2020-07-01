# Running on a treadmill you burn 4.2 calories per minute
# Write a program that displays the number of calories burned after
# 10, 15, 20, 25, and 30 minutes
print("Minutes      Calories")
print("----------------------")
for i in range(10, 31, 5):
    print("{} mins = {:>5} calories".format(i, i * 4.2))

# Take numbers from the user until the user says no
# Ask to say yes or no after every number input.
# Print the average and sum of all numbers entered
