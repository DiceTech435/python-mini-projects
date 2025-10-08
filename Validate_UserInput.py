# Validate user input exercise

# username i no more than 12 characters
# usernae must not contain spaces
# username must not contain digits

username = input("Enter username: ")

if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces")
elif not username.isalpha():
    print("Your username can't contain numbers")
else:
    print(f"Welcome {username}")