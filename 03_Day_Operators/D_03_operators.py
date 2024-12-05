


def main_03_operators():
    print("Hello World!")
    # Declaring the variable at the top first

    a = 7 # a is a variable name and 3 is an integer data type
    b = 3 # b is a variable name and 3 is an integer data type

    # Arithmetic operations and assigning the result to a variable
    total = a + b
    diff = a - b
    product = a * b
    division = a / b
    remainder = a % b
    floor_division = a // b
    exponentiation = a ** b

    # I should have used sum instead of total but sum is a built-in function - try to avoid overriding built-in functions
    print(total) # if you do not label your print with some string, you never know where the result is coming from
    print('total/sum : ', 'a + b = ', total)
    print('diff : ','a - b = ', diff)
    print('Product  : ','a * b = ', product)
    print('division : ','a / b = ', division)
    print('remainder : ','a % b = ', remainder)
    print('floor_division : ','a // b = ', floor_division)
    print('exponentiation : ','a ** b = ', exponentiation)

if __name__ == "__main__":
    print("Entering the main function ...")
    main_03_operators()
    print("Exiting the main function ...")
