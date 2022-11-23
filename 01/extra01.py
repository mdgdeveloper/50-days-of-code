# --- Extra Challenge ---
# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the dictionary.
#
# For example, the following dictionary should return apple as the longest value.

#fruits = {'fruit': 'apple', 'color': 'green'}

# ---

fruits = {'fruit': 'apple', 'color': 'green'}


def longest_value(valueDict):
    length = 0
    currentKey = str("")
    for key, item in valueDict.items():
        if(len(item) > length):
            length = len(item)
            currentKey = str(key)

    return(valueDict[currentKey])


# Basic Testing
result = longest_value(fruits)
print(result)
