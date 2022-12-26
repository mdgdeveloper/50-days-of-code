# Write a function called largest_number that takes a list of
# integers and re-arrange the individual digits to create the largest
# number possible. For example, if you pass the following as an
# argument: list1 = [3, 67, 87, 9, 2]. Your code should return the
# number in this exact format: 9,877,632 as the largest number.

# def largest_number(listNum):
#     result = ""
#     while (len(listNum) > 0):
#         current = 0
#         for value in listNum:
#             if (int(str(value)[0]) > int(str(current)[0])):
#                 current = value
#         result += str(current)
#         listNum.remove(current)

#     return (int(result))


def largest_number(listNum):
    result = []
    for value in listNum:
        aux = [int(d) for d in str(value)]
        for auxVal in aux:
            result.append(auxVal)
    result.sort(reverse=True)
    result = "".join(str(x) for x in result)
    return (f'{int(result):,}')


# Test
list1 = [3, 67, 87, 9, 2]
print(largest_number(list1))
