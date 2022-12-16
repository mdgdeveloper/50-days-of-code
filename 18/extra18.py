# Write a function called add_reverse. This function takes two
# lists as argument and adds each corresponding number, and
# reverses the outcome. For example, if you pass [10, 12, 34]
# and [12, 56, 78]. Your code should return [112, 68, 22]. If the
# two lists are not of equal lengths, the code should return a
# message that "the lists are not of equal lengths".

def add_reverse(list1, list2):
    if(len(list1) != len(list2)):
        return "The lists are not of equal lengths"
    else:
        result = []
        for (k, value) in enumerate(list1):
            result.append(value + list2[k])

    return(result[::-1])


# Test
print(add_reverse([10, 12, 34], [12, 56, 78]))
print(add_reverse([10, 12, 34, 50], [12, 56, 78, 23]))
