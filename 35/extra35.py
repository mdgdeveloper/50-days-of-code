# Write a function called find_index that takes two arguments;
# a list of integers, and an integer. The function should return the
# indexes of the integer in the list. If the integer is not in the list,
# the function should convert all the numbers in the list into the
# given integer.
# For example, if the list is: [1, 2, 4, 6, 7, 7] and the integer is 7,
# your code should return [4, 5] as the indexes of 7 in the list. If
# the list is [1, 2, 4, 6, 7, 7] and the integer is 8, your code should
# return [8, 8, 8, 8, 8, 8] because 8 is not in the list.

def find_index(listInt, idx):
    result = []

    for (k, integer) in enumerate(listInt):
        if (integer == idx):
            result.append(k)

    if (len(result) == 0):
        return [idx] * len(listInt)
    else:
        return result


# Test
print(find_index([1, 2, 4, 6, 7, 7], 7))
print(find_index([1, 2, 4, 6, 7, 7], 8))
