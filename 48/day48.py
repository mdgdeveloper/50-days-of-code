# Write a function called search_binary that searches for the
# number 22 in the following list and returns its index. The
# function should take two parameters, the list and the item that
# is being searched for. Use binary search (iterative Method).

import math


def serach_binary(list, value):
    # To use the binary_search first we need to sort the list:
    list.sort()
    L = 0
    R = len(list) - 1

    while L <= R:
        m = math.floor((L+R)/2)
        if list[m] < value:
            L = m + 1
        elif list[m] > value:
            R = m - 1
        else:
            return m

    return "unsuccessfull"


# Test

list1 = [12, 34, 56, 78, 98, 22, 45, 13]

print(serach_binary(list1, 22))
