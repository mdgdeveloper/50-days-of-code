# Write a function called difference that takes two lists as
# arguments. This function should return all the elements that are
# in list a but not in list b and all the elements in list b not in list
# a. For example:
# list1 = [1, 2, 4, 5, 6]
# list2 = [1, 2, 5, 7, 9]
# should return:
# [4, 6, 7, 9]
# Use list comprehension in your function

def difference(listA, listB):
    list = [x for x in listA if x not in listB] + \
        [x for x in listB if x not in listA]
    return list


# Test
print(difference([1, 2, 4, 5, 6], [1, 2, 5, 7, 9]))
