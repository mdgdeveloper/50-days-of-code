# Write two functions. The first function is called count_words
# which takes a string of words and counts how many words are in
# the string.
# The second function called count_elements takes a string of
# words and counts how many elements are in the string. Do not
# count the whitespaces. The first function will return the number
# of words in a string and the second one will return the number
# of elements (less whitespace). If you pass ‘I love learning’,
# the count_words function should return 3 words and
# count_elements should return 13 elements


def count_words(value):
    return len(value.split(" "))


def count_elements(value):
    valueArray = value.split(" ")
    result = 0
    for word in valueArray:
        result += len(word)

    return result


# Test
print(count_words("I love learning"))
print(count_elements("I love learning"))
