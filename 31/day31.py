# Write a function that has one parameter and takes a list of words
# as an argument. The function returns the longest word from the
# list. Name the function longest_word. The function should
# return the longest word and the number of letters in that word.
# For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your
# function should return
# [10, JavaScript] as the longest word.

def word_length(list):
    length = 0
    value = None
    for (k, word) in enumerate(list):
        if len(word) > length:
            length = len(word)
            value = k

    return([length, list[value]])


# Test
print(word_length(["Java", "JavaScript", "Python"]))
