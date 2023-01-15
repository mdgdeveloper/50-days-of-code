# Write a function called analyse_string that returns the number of
# special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words,
# and, total characters (all letters and special characters minus
# whitespaces) in a string. Return everything in a dictionary format:
# {“special character”: “number”, “words”: “number”, “total
# characters”: “number”}
# Use the string below as an argument:
# “Python has a string format operator %. This functions
# analogously to printf format strings in C, e.g. "spam=%s
# eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".

def analyse_string(sentence):
    special = 0
    words = 0
    total = 0
    for character in sentence:
        if (character == " "):
            continue
        else:
            total += 1
            if (not character.isalpha() and not character.isdigit()):
                special += 1

    words = len(sentence.split(" "))

    return ({
        "special character": special,
        "words": words,
        "total characters": total
    })


# Test
print(analyse_string('“Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2".'))
