# Write a function called spelling_checker. This code asks the
# user to input a word and if a user inputs a wrong spelling it
# should suggest the correct spelling by asking the user if they
# meant to type that word. If the user says no, it should ask the
# user to enter the word again. If the user says yes, it should
# return the correct word. If the word entered by the user is
# correctly spelled the function should return the correct word.
# Use the module textblob.

from textblob import Word


def spelling_checker():
    incorrect = True

    while(incorrect):
        word = input("Provide the word: ")
        w = Word(word)
        results = w.spellcheck()
        if(results[0][1] == 1.0):
            return(word)
        else:
            answer = input(f"Do you mean {results[0][0]}? Yes/No: ")
            if(answer.lower() == "yes"):
                return results[0][0]


# Test

print(spelling_checker())
