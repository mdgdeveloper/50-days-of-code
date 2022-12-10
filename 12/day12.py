# Write a function called count_dots. This function takes a
# string separated by dots as a parameter and counts how many
# dots are in the string. For example, ‘h.e.l.p.’ should return 4
# dots, and ‘he.lp.’ should return 2 dots.

def count_dots(value):
    result = 0
    for char in value:
        if (char == "."):
            result += 1

    return result


# Test
print(count_dots('h.e.l.p.'))
