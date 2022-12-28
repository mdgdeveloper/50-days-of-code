# Write a function called repeated_name that finds the most
# repeated name in the following list.
# name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]


def repeated_name(list):
    resultList = {}
    for value in list:
        if value not in resultList.keys():
            resultList[value] = 1
        else:
            resultList[value] += 1

    return(max(resultList, key=resultList.get))


# Test
name = ["John", "Peter", "John", "Peter", "Jones", "Peter",
        "John", "John", "Peter", "Peter", "Peter", "Peter"]
print(repeated_name(name))
