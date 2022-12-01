# Write a function called prime_numbers. This function asks a
# user to enter a number (integer) as an argument and returns a
# list of all the prime numbers within its range. For example, if user
# enters 10, your code should return [2, 3, 5, 7] as prime numbers

def prime_numbers(maxNum):
    result = []
    for i in range(2, maxNum):
        prime = True
        for k in range(1, i):
            if(i % k == 0 and (i != k and k != 1)):
                prime = False

        if(prime):
            result.append(i)

    return(result)


# Test
print(prime_numbers(10))
