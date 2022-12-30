# Write a function called password_validator. The function
# asks the user to enter a password. A valid password should have
# at least one upper letter, one lower letter, and one
# number. It should not be less than 8 characters long. When
# the user enters a password, the function should check if the
# password is valid. If the password is valid, the function should
# return the valid password. If the password is not valid, the
# function should tell the users the errors in the password and
# prompt the user to enter another password. The code should
# only stop once the user enters a valid password. (use while loop)


def password_validator():
    correct = False
    while (not correct):
        password = input("Introduce the password: ")
        # 1. Check one Upper
        if any(c for c in password if c.islower()):
            # 2. Check one Lower
            if any(c for c in password if c.isupper()):
                # 3. Has a number
                if any(c for c in password if c.isnumeric()):
                    # 4. Length 8
                    if (len(password) > 7):
                        correct = True
                    else:
                        print("Password must be 8 characters long.")
                else:
                    print("Password must contain at least one number")
            else:
                print("Password must contain at least one uppercase character")
        else:
            print("Password must contain at least one lowercase character")

    return password


# Test

print(password_validator())
