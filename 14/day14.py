# Write a function called flat_list that takes one argument, a
# nested list. The function converts the nested list into a onedimension
# list. For example [[2,4,5,6]] should return
# [2,4,5,6].
from itertools import chain


def flat_list(listOfLists):
    result = []
    stack = [listOfLists]
    while stack:
        if isinstance(stack[-1], list):
            try:
                stack.append(stack[-1].pop(0))
            except IndexError:
                stack.pop()  # remove now-empty sublist
        else:
            result.append(stack.pop())
    return result


# test
print(flat_list([[[[2, 4, 5, 6]]]]))
