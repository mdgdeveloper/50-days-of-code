# Write a function called Python_snakes that takes a number
# as an argument and creates the following shape, using the
# number’s range: (hint: Use the loops and emoji library. If you
# pass 7 as argument, your code should print the following:
import emoji


def python_snakes(numb):
    for i in range(numb):
        print("  "*((numb-i)), end="")
        print(emoji.emojize(":snake:")*(2*(i+1)), end="")
        print("")


# tests
python_snakes(7)
