# Write a function called create_user. This function asks the
# user to enter their name, age, and password. The function
# saves this information in a dictionary. For example, if the use
# enters name as Peter, age - 18 and password - love. The
# function should save the information as: {'name': 'Peter',
# 'age': 18, 'password': 'love'}
# Once the information is saved. The function should print to the
# user that - "User saved. Please login"
# The function should then ask the user to re-enter their name
# and password. If the name and password match with what is
# saved in the dictionary, the function should return "Logged in
# successfully". If the name and password do not match with
# what is saved in the dictionary, the function should print
# ('Wrong password or user name. Please try again'. The
# function should keep running until the user enters correct
# logging details.


def create_user():
    userDB = {}
    userDB["name"] = input("Introduce your username: ")
    userDB["age"] = input("Introduce your age: ")
    userDB["password"] = input("Introduce the password: ")

    print("User saved. Please login.")
    login = False
    while(not login):
        name = input("Please, introduce your name: ")
        password = input("Please, introduce your password: ")

        if(userDB["name"] == name and userDB["password"] == password):
            print("Logged in successfully")
            login = True
        else:
            print("Wrong password or user name. Please try again.")


# Test
create_user()
