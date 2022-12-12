# A school has asked you to write a program that will calculate
# teachers' salaries. The program should ask the user to enter the
# teacher’s name, the number of periods taught in a month,
# and the rate per period. The monthly salary is calculated by
# multiplying the number of periods by the monthly rate.
# The current monthly rate per period is $20. If a teacher has
# more than 100 periods in a month, everything above 100 is
# overtime. Overtime is $25 per period. For example, if a teacher
# has taught 105 periods, their monthly gross salary should be
# 2,125. Write a function called your_salary that calculates a
# teacher’s gross salary. The function should return the
# teacher’s name, periods taught, and gross salary. Here is
# how you should format your output:
# Teacher: John Kelly,
# Periods: 105
# Gross salary:2,125

def your_salary():
    name = str(input("Introduce teacher's name: "))
    periods = int(input("Introduce periods number: "))

    overtime = periods - 100
    salary = 0
    if overtime > 0:
        salary = 20*100 + 25*overtime
    else:
        salary = 20*periods

    print(f"Teacher: {name},")
    print(f"Periods: {periods},")
    print(f"Gross salary: {salary:,}")


# test
your_salary()
