# names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

# You are given a list of names above. This list is made up of names
# of lowercase and uppercase letters. Your task is to write a code
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted
# alphabetically in descending order. Using the list above, your
# code should return:
# ('kerry', 'dickson', 'carol', 'adam')

def lowercase_names(nameList):
    result = ()
    for name in nameList:
        if name.islower():
            result += (name,)

    resultSorted = sorted(result, reverse=True)

    return (resultSorted)


# Test
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
print(lowercase_names(names))
