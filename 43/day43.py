# Write a function called student_marks that records marks
# achieved by students in a test. The function should ask the user
# to input the name of the student and then ask the user to input
# the marks achieved by the student. The information should be
# stored in a dictionary. The name is the key and the marks is the
# value. When the user enters done, the function should return a
# dictionary of names and values entered.

def student_marks():
    name = ""
    result = dict()

    while(name != "done"):
        name = input("Introduce the name of the student: ")
        if(name == "done"):
            break
        marks = float(input(f"Introduce the marks for {name}: "))
        result[name] = marks
    return result


# Test

print(student_marks())
