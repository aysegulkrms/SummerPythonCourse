# Allowed users to login
allowed_users = ["Bill", "Steve", "Michael", "Cemil"]
passwords = ["123456"]

username = input("What is your login? ")


if username in allowed_users:
    password = input("What is your password?")
    if password in passwords:
        print("Access Granted")
else:
    print("Access Denied, username is incorrect")

# If password and username are matching they will be granted access
