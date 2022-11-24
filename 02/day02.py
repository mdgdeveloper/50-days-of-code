# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list.
#
# For example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and summed to 9.

def convert_add(listString):
    resultList = []
    result = 0
    for value in listString:
        newValue = int(value)
        resultList.append(newValue)
        result = result + newValue

    return([resultList, result])


# Test
testList = []
value = input("Introduce a number (press enter to end): ")
while(value):
    testList.append(value)
    value = input("Introduce a number (press enter to end): ")

result = convert_add(testList)

print(result)
