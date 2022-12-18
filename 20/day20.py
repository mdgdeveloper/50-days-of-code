# Write a function called capitalize. This function takes a string
# as an argument and capitalizes the first letter of each word. For
# example, ‘i like learning’ becomes ‘I Like Learning’.

def capitalize(sentence):
    phrase = sentence.split(" ")
    result = []
    for a in phrase:
        word = a.lower()
        word_list = list(word)
        word_list[0] = word_list[0].upper()
        result.append("".join(word_list))

    return " ".join(result)


# Test
print(capitalize("i like learning"))
