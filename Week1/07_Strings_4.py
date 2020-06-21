# The Strip() Method removes any whitespaces from beginning or the end
name = "   Cemil Koc    "
print(name)
print(name.strip())

# The replace method replaces a string with another string:
text = "Welcome to the world of Python"
print(text.replace("Python", "Java"))

# Title method capitalizes each word
city = "Around 50 tons of paint are added to eiffel tower every 7 years"
print(city.title())

# Challenge ! Split the email address by @ symbol
prof_address = "michael@nyu.edu"
print(prof_address.split("@"))

# Challenge ! Replace the dots(.) with slashes(/)
birthday = "09.14.1995"
print(birthday.replace(".", "/"))
