# Write a function called hide_password that takes no
# parameters. The function takes an input (a password) from a
# user and returns a hidden password. For example, if the user
# enters ‘hello’ as a password the function should return ‘****’ as
# a password and tell the user that the password is 4 characters
# long.


def hide_password(password):
    password_result = "*" * len(password)
    print(f"The password {len(password)} characters long.")
    return (password_result)


# Test
password = str(input("Input a password: "))
print(hide_password(password))
