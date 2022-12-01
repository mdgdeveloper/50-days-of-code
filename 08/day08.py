# Write a function called odd_even that has one parameter and
# takes a list of numbers as an argument. The function returns the
# difference between the largest even number in the list and the
# smallest odd number in the list. For example, if you pass
# [1,2,4,6] as an argument the function should return 6 -1= 5.

def odd_even(listNum):
    odd = []
    even = []
    for num in listNum:
        if (num % 2):
            odd.append(num)
        else:
            even.append(num)

    maxNum = max(even)
    minNum = min(odd)
    return(maxNum - minNum)


# test
print(odd_even([1, 2, 4, 6]))
