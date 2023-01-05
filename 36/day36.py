# Write a function called count that takes one argument a string,
# and returns a dictionary of how many times each element
# appears in the string. For example, ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.

def count(word):
    result = {}
    for char in word:
        if(char in result):
            result[char] += 1
        else:
            result[char] = 1
    return result


# Test
print(count("hello"))
