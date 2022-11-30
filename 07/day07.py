# Write a function called string_range that takes a single
# number and returns a string of its range. The string characters
# should be separated by dots(.) For example, if you pass 6 as
# an argument, your function should return ‘0.1.2.3.4.5’.


def string_range(number):
    result = "0"
    for i in range(number):
        result += f".{i+1}"
    return result


# Test
print(string_range(5))
