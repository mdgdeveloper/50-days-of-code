# list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
# 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
# Write a function called missing_numbers that takes a list of
# sequence of numbers and finds the missing numbers in the
# sequence. The list above should return:
# [4, 8, 10, 13, 16, 29, 30]


def missing_numbers(listNum):
    listNum.sort()
    last = listNum[-1]
    result = []
    for i in range(last):
        if i not in listNum and i != -0:
            result.append(i)

    return result


# Test
list = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15,
        17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]
print(missing_numbers(list))
