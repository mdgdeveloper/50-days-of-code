# Create a simple calculator. The calculator should be able to perform
# basic math operations, add, subtract, divide and multiply. The
# calculator should take input from users. The calculator should be
# able to handle ZeroDivisionError, NameError, and
# ValueError.

def simple_calculator():
    result = 0
    operations = {
        "add": "+",
        "sub": "-",
        "div": "/",
        "mul": "*"
    }

    try:
        operation = input(
            "Introduce de operation: [add, sub, div, mul] ").lower()
        if(operation != "add" and operation != "sub" and operation != "div" and operation != "mul"):
            raise ValueError("Wrong operation")
    except ValueError:
        print("You have selected a wrong operation.")
        return False

    try:
        operand1 = int(input("Introduce the first operand: "))
        operand2 = int(input("Introduce the second operand: "))
        operationDefined = f"{operand1} {operations[operation]} {operand2}"
        result = eval(operationDefined)
    except ValueError:
        print("Wrong values introduced")
        return False
    except NameError:
        print("Missing variables")
        return False
    except ZeroDivisionError:
        print("You cannot divide by 0!")
        return False
    return result


# Test
print(simple_calculator())
