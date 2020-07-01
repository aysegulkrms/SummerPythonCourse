for i in range(6):
    print("*", end="")  # ******

for rows in range(5):
    print()
    for cols in range(6):
        print("*", end="")

# Challenge
# Ask for how many rows?
# Ask for how many columns?
# Print the stars according to the user input
print()
rows = int(input("How many rows? "))
cols = int(input("How many cols? "))

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()

print("\n")
for i in range(8):
    for j in range(i + 1):
        print("*", end="")
    print()

# *
# **
# ***
# ****
# *****