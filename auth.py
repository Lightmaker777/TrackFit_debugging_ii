# Task 1:

# In auth.py to make the code more efficient adding a recursive function that asks again for a username and password if the credentials are wrong.

# Function to authenticate the user by requesting username and password
def authenticate_user():
    # fixed grammatical failure
    username = input("Please give your username: ")
    # fixed grammatical failure
    password = input("Please give your password: ")
    print("Thank you for logging in!")
    print()
    # Check if the provided credentials are correct (username: "admin", password: "password")
    if username == "admin" and password == "password":  # changed 'or' to 'and' to make it more efficient
        return True
    else:
        # Removed 'return False' and made the recursive function by adding 'return' before 'authenticate_user()'
        # If the credentials are incorrect, ask the user to enter valid credentials recursively
        print("Please enter the valid credentials! ")
        print()
        return authenticate_user()
