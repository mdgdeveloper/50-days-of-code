# Create a function called count_the_vowels. The function
# takes one argument, a string, and returns the number of vowels
# in the string. For example, ‘hello’ should return 2 vowels. If a
# vowel appears in a string more than once it should be counted
# as one. For example, ‘saas’ should return 1 vowel. Your code
# should count lowercase and uppercase vowels


def count_the_vowels(sentence):
    result = ["a", "e", "i", "o", "u"]
    for character in sentence:
        if character.lower() in ('a', 'e', 'i', 'o', 'u'):
            if character.lower() in result:
                result.remove(character.lower())

    return (5 - len(result))


# Test
print(count_the_vowels("abeiolu"))
