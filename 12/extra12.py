# Write a function called age_in_minutes that tells a user how
# old they are in minutes. Your code should ask the user to
# enter their year of birth, and it should return their age in
# minutes (by subtracting their year of birth to the current year).
# Here are things to look out for:
# a. The user can only input a 4-digit year of birth. For
# example, 1930 is a valid year. However, entering any
# number longer or less than 4 digits long should render
# input invalid. Notify the user to input a four digits
# number.
# b. If a user enters a year before 1900, your code should
# tell the user that input is invalid. If the user enters the
# year after the current year, the code should tell the user,
# to input a valid year.
# The code should run until the user inputs a valid year.
# Your function should return the user's age in minutes. For
# example, if someone enters 1930, as their year of birth your
# function should return:
from datetime import date


def age_in_minutes():
    current_year = date.today().year
    year = 0
    while (len(str(year)) != 4):
        year = int(input('Introduce your year of birth: '))
        if (len(str(year)) != 4):
            print("Error: Year must be 4 digits long")
        else:
            if (year < 1900):
                year = 0
                print("Error: Year must be above 1900")
            if (year > current_year):
                year = 0
                print("Error: Year cannot be in the future!")

    d0 = date(current_year, 1, 1)
    d1 = date(year, 1, 1)
    diff = d0 - d1
    # This is the solution expected, but does not take into consideration leap years.
    diff2 = (current_year - year)*365*24*60
    return f"You are {diff.days*24*60} minutes old."


# Test
print(age_in_minutes())
