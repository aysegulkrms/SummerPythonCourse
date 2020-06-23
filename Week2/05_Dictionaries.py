# Dictionary can be created using curly braces {} separated by commas.
# An item has a key and a value that is expressed as a pair {key: value}

# lists [], tuples (), dictionaries {}

# Empty Dictionary
my_dictionary = {}
print(my_dictionary)

# My dictionary with integer keys {key: value}
my_dictionary_2 = {1: 'apple', 2: 'banana', 3: 'orange'}

personal_details = {'name': "Cemil", 'last_name': 'Koc', 'age': 25}
print(personal_details)
print(personal_details['name'])

# Dictionary with mixed keys
my_dictionary_3 = {'name': "Michael", 3: [1, 2, 3]}

# using dict()
my_dictionary_4 = dict({1: 'apple', 2: 'pear'})

MLB_teams = dict([('Colorado', 'Rockies'), ('Boston', 'Red Sox'), ('California', 'Dodgers')])
print(MLB_teams)

# get vs [] for retrieving elements
print(MLB_teams['Boston'])

# get
print(MLB_teams.get('California'))

# Changing and Adding Dictionary Elements
my_dictionary_5 = {'name': 'Cemil', 'age': 25}
my_dictionary_5['age'] = 26
print(my_dictionary_5)

# Adding an element
my_dictionary_5['address'] = 'Montclair'
print(my_dictionary_5)

# Removing elements from dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)

print(squares.popitem())
print(squares)

print(squares.clear())
print(squares)
