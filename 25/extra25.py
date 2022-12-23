# str1 = "the love is real"
# Write a function called read_backwards that takes a string as
# an argument and reverses it. For example, the string above
# should return: "real is love the"

def read_backwards(sentence):
    result = []
    sentenceArr = sentence.split(" ")
    for i in range(len(sentenceArr)):
        result.append(sentenceArr[len(sentenceArr)-1-i])

    return (" ".join(result))


# Test
str1 = "the love is real"
print(read_backwards(str1))
