# s = "love live and laugh"
# Write a function called multiply_words that takes a string as an
# argument and multiplies the length of each word in the string by
# the length of other words in the string. For example, the string
# above should return 240 - love (4) live (4) and (3) laugh (5).
# However, your function should only multiply words will all
# lowercase letters. If a word has one upper case letter, it should be
# ignored. For example, the following string:
# s = "Hate war love Peace" should return 12 – war (3) love (4).
# Hate and Peace will be ignored because they have at least one
# uppercase letter.

def multiply_words(value):
    sentence = value.split(" ")
    result = 1
    for word in sentence:
        if(word.islower()):
            result = result * len(word)

    return result


# Test
s = "love live and laugh"
s2 = "Hate war love Peace"
print(multiply_words(s))
print(multiply_words(s2))
