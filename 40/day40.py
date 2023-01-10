# Write a function called translate that takes the following
# words and translates them into pig Latin.
# a = 'i love python'
# Here are the rules:
# 1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the
# end. For example, ‘eat’ will become ‘eatyay’
# 2. If a word starts with anything other than a vowel, move
# the first letter to the end and add ‘ay’ to the end. For
# example, ‘day’ will become ‘ayday’.
# Your code should return:
# iyay ovelay ythonpay

def translate(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    # Split the words into a list
    sentenceArr = sentence.split(" ")
    result = []
    for word in sentenceArr:
        # Case starts with vowel
        if (word[0].lower() in vowels):
            word = word + "yay"
            result.append(word)
        else:
            word = word[1:] + word[0] + "ay"
            result.append(word)

    return " ".join(result)


# Test
a = 'i love python'
print(translate(a))
