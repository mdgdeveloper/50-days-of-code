# Write a function called any_number that can receive any
# number of arguments (integers and floats) and return the
# average of those integers. If you pass 12, 90, 12, 34 as
# arguments your function should return 37.0 as average. If you
# pass 12, 90 your function should return 51.0 as average.

def any_number(*args):
    total = 0
    num = 0
    for n in args:
        total += n
        num += 1

    return total/num


# Test
print(any_number(12, 90, 12, 34))
print(any_number(12, 90))
