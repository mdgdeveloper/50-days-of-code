# Create three functions. The first called add_hash takes a string and
# adds a hash # between the words. The second function called
# add_underscore removes the hash (#) and replaces it with an
# underscore "_" The third function called remove_underscore,
# removes the underscore and replaces it with nothing. if you pass
# ‘Python’ as an argument for the three functions, and you call them at
# the same time like:
# print(remove_underscore(add_underscore(add_hash('Python'))))
# it should return ‘Python’.

def add_hash(value):
    sentence = value.split(" ")
    result = []
    for word in sentence:
        result.append(word)
        result.append("#")

    del result[-1]

    return ("".join(result))


def add_underscore(value):
    sentence = list(value)
    for (k, char) in enumerate(sentence):
        if char == "#":
            sentence[k] = "_"

    return "".join(sentence)


def remove_underscore(value):
    result = value.replace("_", " ")
    return result


# Test
print(remove_underscore(add_underscore(add_hash("Testing the system"))))
print(remove_underscore(add_underscore(add_hash("Python"))))
