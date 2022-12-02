# Write a function called zeros_last. This function takes a list as
# argument. If a list has zeros (0), it will move them to the front of
# the list and maintain the order of the other numbers in the list.
# If there are no Zeros in the list, the function should return the
# original list sorted in ascending order. For example, if you pass
# [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
# 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
# your code should return [1, 2, 4, 6, 7].

def zeros_last(listNum):
    zeroCount = 0
    for (index, x) in enumerate(listNum):
        if x == 0:
            zeroCount += 1
            listNum.pop(index)

    if (zeroCount > 0):
        for i in range(zeroCount):
            listNum.append(0)
    else:
        listNum.sort()

    return listNum


# Test
print(zeros_last([1, 4, 6, 0, 7, 0, 9]))
print(zeros_last([2, 1, 4, 7, 6]))
