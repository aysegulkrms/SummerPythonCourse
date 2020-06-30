# Counting the vowels of a String

user_input = input("Please enter a word or a sentence: ")

vowels = ['a', 'e', 'i', 'o', 'u']

count = 0

for i in user_input:
    if i.lower() in vowels:
        count = count + 1

print("Your input has {} vowels".format(count))
