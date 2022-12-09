# Write a function called equal_strings. The function takes two
# strings as arguments and compares them. If the strings are equal
# (if they have the same characters and have equal length), it
# should return True, if they are not, it should return False. For
# example, ‘love’ and ‘evol’ should return True.

def equal_strings(string1, string2):
    if(len(string1) != len(string2)):
        return False
    else:
        string1 = sorted(string1)
        string2 = sorted(string2)
        for i in range(len(string1)):
            if (string1[i] != string2[i]):
                return False

        return True


# Test
print(equal_strings("love", "evol"))
