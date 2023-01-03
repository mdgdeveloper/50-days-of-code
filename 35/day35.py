# Write a function called check_pangram that takes a string
# and checks if it is a pangram. A pangram is a sentence that
# contains all the letters of the alphabet. If it is a pangram,
# the function should return True, otherwise, return False. The
# following sentence is a pangram so it should return True:
# 'the quick brown fox jumps over a lazy dog

def check_pangram(sentence):
    alphabet = list("abcdefghijklmnopqrstuvw")
    sentence = sentence.replace(" ", "")
    for char in sentence:
        if (char in alphabet):
            alphabet.remove(char)

    if (len(alphabet) == 0):
        return True
    else:
        return False


# Test

print(check_pangram("the quick brown fox jumps over a lazy dog"))
