# Write a function called make_tuples that takes two lists,
# equal lists, and combines them into a list of tuples. For
# example, if list a is [1,2,3,4] and list b is [5,6,7,8], your
# function should return [(1,5), (2,6), (3,7), (4,8)].

def make_tuples(listA, listB):
    # We are assuming that both lists have the same length
    result = []
    for (k, value) in enumerate(listA):
        tuple = (value, listB[k])
        result.append(tuple)
    return result


# Test
print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8]))
