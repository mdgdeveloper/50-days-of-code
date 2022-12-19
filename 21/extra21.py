# Write a function called even_or_average that ask a user to
# input five numbers. Once the user is done, the code should
# return the largest even number in the inputted numbers. If
# there is no even number in the list, the code should return the
# average of all the five numbers.

def even_or_average():
    total = 5
    values = []
    while(total > 0):
        value = int(input("Introduce a number: "))
        values.append(value)
        total -= 1

    values.sort(reverse=True)
    total = 0
    for n in values:
        total += n
        if(n % 2 == 0):
            return n

    return(total/len(values))


# Test
print(even_or_average())
