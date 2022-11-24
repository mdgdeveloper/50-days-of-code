# Write a function called check_duplicates that takes a list of  strings as an argument. The function should check if the list has
# any duplicates. If there are duplicates, the function should return  the duplicates.
# If there are no duplicates, the function should  return "No duplicates".
#
# For example, the list of fruits below should return apple as a duplicate and list of names should  return "no duplicates".
# fruits = ['apple', 'orange', 'banana', 'apple']
# names = ['Yoda', 'Moses', 'Joshua', 'Mark']

def check_duplicates(valueList):
    result = []
    for i, value1 in enumerate(valueList):
        for value2 in valueList[i+1::]:
            if(value1 == value2):
                result.append(value1)
                valueList.remove(value1)

    if(len(result) == 0):
        return("No duplicates")
    else:
        return(result)

# Test


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']

print(check_duplicates(fruits))
print(check_duplicates(names))
