# names = [ "Peter", "Jon", "Andrew"]
# Write a function called sort_length that takes a list of strings
# as an argument, and sorts the strings in ascending order
# according to their length. For example, the list above should
# return:
# ['Jon', 'Peter', 'Andrew']
# Do not use the built-in sort functions

def sort_length(strList):
    # Using the bubble sorting algorithm
    for i in range(len(strList)):
        for j in range(len(strList)-i-1):
            if(len(strList[j]) > len(strList[j+1])):
                temp = strList[j]
                strList[j] = strList[j+1]
                strList[j+1] = temp
    return(strList)


# Test
names = ["Peter", "Jon", "Andrew"]

print(sort_length(names))
