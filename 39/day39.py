# Create a function called generate_password that generates any
# length of password for the user. The password should have a
# random mix of upper letters, lower letters, numbers, and
# punctuation symbols. The function should ask the user how
# strong they want the password to be. The user should pick from -
# weak, strong, and very strong. If the user picks weak, the
# function should generate a 5-character long password. If the user
# picks strong, generate an 8-character password and if they pick
# very strong, generate a 12-character password.

import random
import string


def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    level = input(
        "Which level of security do you want? (weak/strong/very strong): ")

    if(level.lower() == "weak"):
        length = 5
    elif(level.lower() == "strong"):
        length = 8
    else:
        length = 12

    password = "".join(random.choice(letters + digits + punctuation)
                       for i in range(length))

    return password


# Test
print(generate_password())
