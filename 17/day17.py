# Write a function called user_name, that creates a username
# for the user. The function should ask a user to input their name.
# The function should then reverse the name and attach a
# randomly issued number between 0 – 9 at the end of the name.
# The function should return the username.
import random


def user_name():
    name = input('Introduce your name: ')
    username_base = name[::-1].lower()
    number = random.randint(0, 9)
    return(username_base + str(number))


# Test
print(user_name())
