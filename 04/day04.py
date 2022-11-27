# Write a function called only_floats, which takes two
# parameters a and b, and returns 2 if both arguments are floats,
# returns 1 if only one argument is a float, and returns 0 if neither
# argument is a float. If you pass (12.1, 23) as an argument, your
# function should return a 1.

def only_floats(a, b):
    total = 0
    if (type(a) is float):
        total += 1
    if (type(b) is float):
        total += 1
    return total


# test
print(only_floats(12.2, 23))
