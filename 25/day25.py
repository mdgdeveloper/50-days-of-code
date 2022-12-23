# Create a function called all_the_same that takes one
# argument, a string, a list, or a tuple and checks if all the
# elements are the same. If the elements are the same, the function
# should return True. If not, it should return False. For example,
# [‘Mary’, ‘Mary’, ‘Mary’] should return True.

def all_the_same(list):
    for i in range(len(list)-1):
        if (list[i] != list[i+1]):
            return False

    return True


# Test
print(all_the_same(("test", "tsest")))
