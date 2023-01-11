# Create a function called words_with_vowels, this function
# takes a string of words and returns a list of only words that have
# vowels in them. For example, ‘You have no rhythm’ should
# return [‘You’,’have’, ‘no’].

def words_with_vowels(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    sentenceArr = sentence.split(" ")
    result = []
    for word in sentenceArr:
        for vowel in vowels:
            if vowel in word and word not in result:
                result.append(word)
    return result


# Test
text = "You have no rhythm"

print(words_with_vowels(text))
