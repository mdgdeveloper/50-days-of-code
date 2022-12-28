# You work for a local school in your area. The school has a list of
# names of students saved in a list. The school has asked you to
# write a program that takes a list of names and sorts them
# alphabetically. The names should be sorted by last names. Here
# is a list of names:
# [‘Beyonce Knowles, ‘Alicia Keys’, ‘Katie Perry’, ‘Chris
# Brown’,’ Tom Cruise’]
# Your code should not just sort them alphabetically, but it should
# also switch the names (the last name must be the first). Here is
# how your code output should look:
# ['Brown Chris', 'Cruise Tom', 'Keys Alicia', 'Perry Katie',
# 'Knowles Beyonce']
# Write a function called sorted_names.

def sorted_names(listNames):
    result = []
    for name in listNames:
        aux = name.split(" ")
        newName = aux[1] + " " + aux[0]
        print(newName)
        result.append(newName)

    result.sort()
    return(result)


# Test
print(sorted_names(["Beyonce Knowles", "Alicia Keys",
      "Katie Perry", "Chris Brown", "Tom Cruise"]))
