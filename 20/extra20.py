# You are given a string of words. Some of the words in the string
# contain uppercase letters. Write a code that will return all the
# words that have an uppercase letter. Your code should return a
# list of the words. Each word in the list should be reversed. Here
# is how your output should look:
# ['gninrAel', 'tUb', 'uoY', 'yLppa', 'flesRuoy', 'eVeihca']

def reversed_list(sentence):
    phrase = sentence.split(" ")
    result = []
    for word in phrase:
        word_list = list(word)
        upper = False
        for char in word_list:
            if (char.isupper()):
                upper = True
        if (upper):
            result.append("".join(word[::-1]))

    return (result)


# Test
str1 = 'leArning is hard, bUt if You appLy youRself ' \
    'you can achieVe success'
print(reversed_list(str1))
