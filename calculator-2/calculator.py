"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
# create a while true loop
# ask the user for input - which operation do they want to use 
# make if and elif statements for each option 
# keep asking for an input
# stop the loop when the user enter "q"

while True:
    user_input = input("What would you like to do? ")
    tokens = user_input.split(" ")

    if "q" in tokens:
        print("You will exit")
        break

    if len(tokens) != 3:
        print("You need to enter the operator and two numbers.")
        continue

    operator = tokens[0]
    num_1 = tokens [1]
    num_2 = tokens [2]
    result = None

    if not num_1.isdigit() and not num_2.isdigit():
        print("Please enter 1 operator and 2 digit")
        continue

    if operator == "+":
        result = add(float(num_1),float(num_2))

    elif operator == "-":
        result = subtract(float(num_1),float(num_2))

    elif operator == "*":
        result = multiply(float(num_1),float(num_2))

    elif operator == "/":
        result = divide(float(num_1),float(num_2))

    elif operator == "square":
        result = square(float(num_1))
    
    elif operator == "cube":
        result = cube(float(num_1))

    elif operator == "pow":
        result = power(float(num_1),float(num_2))

    elif operator == "mod":
        result = mod(float(num_1),float(num_2))

    elif operator == 'x+':
        result = add_mult(float(num1), float(num2), float(num3))

    elif operator == 'cubes+':
        result = add_cubes(float(num1), float(num2))

    else:
        result = 'Please enter an operator followed by two integers.'


    print(result)
