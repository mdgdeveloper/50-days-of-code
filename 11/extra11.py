# Write a function called swap_values. This function takes a list
# of numbers and swaps the first element with the last element.
# For example, if you pass [2, 4,67, 7] as a parameter, your
# function should return
# [7, 4, 67, 2].

def swap_vallues(list):
    last = list[len(list)-1]
    list[len(list)-1] = list[0]
    list[0] = last

    return list


# Test
print(swap_vallues([2, 4, 67, 7]))
