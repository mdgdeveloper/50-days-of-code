# Write a function called sum_list with one parameter that takes
# a nested list of integers as an argument and returns the sum of
# the integers. For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]]
# as an argument your function should return a sum of 33.

def sum_list(listNum):
    flat_list = [item for sublist in listNum for item in sublist]
    result = 0
    for item in flat_list:
        result += item

    return result


# Test
print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
