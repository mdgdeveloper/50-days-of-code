# Write a function called your_vat. The function takes no
# parameter. The function asks the user to input the price of an
# item and VAT (vat should be a percentage). The function should
# return the price of the item plus VAT. If the price is 220 and,
# VAT is 15% your code should return a vat inclusive price of 253.
# Make sure that your code can handle ValueError. Ensure the
# code runs until valid numbers are entered. (hint: Your code
# should include a wh

def your_vat():
    try:
        value = int(input("Introduce the price of the item: "))
        vat = input("Introduce the VAT percentage: ")
        if "%" not in vat:
            raise ValueError("VAT should be a percentage")
        vat_value = int(vat[:-1])/100
        return ((value)*(1+vat_value))
    except ValueError as e:
        print(e)
        return False


# Test
print(your_vat())
