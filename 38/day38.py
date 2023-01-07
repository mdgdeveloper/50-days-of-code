# Write a function called guess_a_number. The function
# should ask a user to guess a randomly generated number. If the
# user guesses a higher number, the code should tell them that the
# guess is too high, if the user guesses low, the code should tell
# them that their guess is too low. The user should get a maximum
# of three guesses. When the user guesses right, the code should
# declare them a winner. After three wrong guesses, the code
# should declare them a loser.

# Import randomizer library
# This library provides pseudo-random numbers
import random


def guess_a_number():
    value = random.randint(0, 10)
    tries = 0
    guess = -1
    while (tries < 3):
        guess = int(input("Try to guess the number: "))
        if (guess > value):
            print("The number you selected is higher than the solution")
        else:
            if (guess < value):
                print("The number you selected is lower than the solution")
            else:
                return (f"You find it!! The value was: {value}")
        tries += 1
        print(f"You have {3-tries} remaining tries")

    return (f"You loose the game! The value was: {value}")


# Test
print(guess_a_number())
