# Create a function called biggest_odd that takes a string of
# numbers and returns the biggest odd number in the list. For
# example, if you pass ‘23569’ as an argument, your function
# should return 9. Use list comprehension

# We assume that the list of numbers are only of ONE digit


def biggest_odd(numList):
    newList = [int(x) for x in numList if int(x) % 2 != 0]
    return (max(newList))


# test
print(biggest_odd("23569"))
