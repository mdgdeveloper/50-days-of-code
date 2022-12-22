# Create a function called average_calories that calculates the
# average calories intake of a user. The function should ask the user
# to input their calories intake for any number of days and once they
# hit ‘done’ it should calculate and return the average intake.

def average_calories():
    value = ""
    total = 0
    count = 0
    while(value != "done"):
        value = input("Introduce the calories intake [done for finish]: ")
        if(value.isnumeric()):
            total += float(value)
            count += 1

    return(total/count)


# Test
print(average_calories())
