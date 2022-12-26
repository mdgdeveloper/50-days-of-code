# Write a function called index_position. This function takes a
# string as a parameter and returns the positions or indexes of all
# lower letters in the string. For example, ‘LovE’ should return
# [1,2].

def index_position(value):
    result = []
    for (k, char) in enumerate(value):
        if (char.islower()):
            result.append(k)

    return result


# Test

print(index_position("LovE"))
