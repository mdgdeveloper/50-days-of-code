# You are given a list of names, and you are asked to write a code
# that returns all the names that start with ‘S’. Your code should
# return a dictionary of all the names that start with S and how
# many times they appear in the dictionary. Here is a list below:
# names = ["Joseph","Nathan", "Sasha", "Kelly",
# "Muhammad", "Jabulani", "Sera”, "Patel", "Sera”]
# Your code should return: {“Sasha”: 1, “Sera”: 2}

def dictionary_names(list):
    result = {}
    for value in list:
        if value[0].lower() == "s":
            if(current := result.get(value)):
                result.update({f"{value}": current+1})
            else:
                result.update({f"{value}": 1})
    return result


# test
print(dictionary_names(["Joseph", "Nathan", "Sasha",
      "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]))
