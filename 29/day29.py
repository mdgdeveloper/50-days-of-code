# Write a function called middle_figure that takes two
# parameters a, and b. The two parameters are strings. The
# function joins the two strings and finds the middle element.
# If the combined string has a middle element, the function should
# return the element, otherwise, return ‘no middle figure’. Use
# ‘make love’ as an argument for a and ‘not wars’ as an
# argument for b. Your function should return ‘e’ as the middle
# element. Whitespaces should be removed.
import math


def middle_figure(a, b):
    a = a.replace(" ", "")
    b = b.replace(" ", "")

    word = a + b
    if (len(word) % 2 == 0):
        return "no middle figure"
    else:
        mid = int(math.floor(len(word)/2))
        return word[mid]


# Test
print(middle_figure("make love", "not wars"))
