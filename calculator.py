# Python implementation of a basic five-function calculator
# Can do addition, substraction, mutiplication, division, and modulus
# The calculator accepts positive, negative, and zero-value floating point numbers


# ---------- Interface ----------

# User enters a number, followed by a sign (+, -, *, /, %), followed by another number. The result is used as the first
# number for the next equation. The user can reset the calculator by entering "clear" into the sign prompt. The
# user can quit the calculator by entering "quit" into the sign prompt, which will end the process. The calculator
# also quits automatically if the result of an equation is undefined (div or mod by 0)


def interface():
    sign = ""
    while sign != "quit":
        sign = ""

        # Handles user inputs that cannot be converted to floating point values (non-number inputs)
        try:
            first = float(input("Enter first number: ")) 
        except ValueError:          
            print("Invalid entry.")
            return
        while sign != "clear":
            sign = input("Enter sign: ")

            # Addition
            if sign == "+":
                try:
                    second = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid entry.")
                    return
                first = add(first, second)
                print(first)
            # Subtraction
            elif sign == "-":
                try:
                    second = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid entry.")
                    return
                first = sub(first, second)
                print(first)
            # Multiplication
            elif sign == "*":
                try:
                    second = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid entry.")
                    return
                first = mult(first, second)
                print(first)
            # Division
            elif sign == "/":
                try:
                    second = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid entry.")
                    return
                first = div(first, second)
                print(first)
                # Handles undefined results (division by 0)
                if first == "Undefined":
                    return
            # Modulus
            elif sign == "%":
                try:
                    second = float(input("Enter second number: "))
                except ValueError:
                    print("Invalid entry.")
                    return
                first = mod(first, second)
                print(first)
                # Handles undefined results (mod by 0)
                if first == "Undefined":
                    return
            # Reset calculator
            elif sign == "clear":
                break
            # Quit calculator
            elif sign == "quit":
                return
            # User entered an invalid sign
            else:
                print("Invalid sign")
                return


# ---------- Operations ----------

# Add two numbers
def add(a, b):
    return a + b


# Substract two numbers
def sub(a, b):
    return a - b


# Multiply two numbers
def mult(a, b):
    return a * b


# Divide two numbers. Dividing by 0 is not allowed
def div(a, b):
    if b == 0:
        return "Undefined"
    return a / b


# Modulus of two numbers, or the remainder of the first divided by the second.
def mod(a, b):
    if b == 0:
        return "Undefined"
    return a % b


# Run
interface()