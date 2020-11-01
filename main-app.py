from calculator import Calculator

def calcMenu():
    print("""
        TEAM COCOA CALCULATOR PROGRAM
    TODAYS SPECIALS: 
    1) ADD
    2) SUBTRACT
    3) MULTIPLY
    4) DIVIDE
    5) SQUARE
    6) SQUARE ROOT
    7) EXPONENTS
    8) EXIT
    """)
    choice = int(input("PLEASE ENTER A NUMBER BETWEEN 1 - 8: \n"))
    return choice

def getAddNum():
    a = float(input("Enter the first number that you want to add: \n"))
    b = float(input("Enter the second number that you want to add: \n"))
    return a, b

def getSubNum():
    a = float(input("Enter the first number that you want to subtract: \n"))
    b = float(input("Enter the second number that you want to subtract: \n"))
    return a, b

def getMultiNum():
    a = float(input("Enter the first number that you want to multiply: \n"))
    b = float(input("Enter the second number that you want to multiply: \n"))
    return a, b

def getDivNum():
    a = float(input("Enter the first number that you want to divide: \n"))
    b = float(input("Enter the second number that you want to divide: \n"))
    return a, b

def getSquared():
    a = float(input("Enter the number that you want to square: \n"))
    b = float(input("Enter the second number that you want to square: \n"))
    return a, b

def getRoot():
    a = float(input("Enter the number that you want to find the square root of : \n"))
    return a

def getExponent():
    a = float(input("Enter the base number : \n"))
    b = float(input("Enter the exponent number : \n"))
    return a, b


# def getTwoNumbers():
#     a = float(input("first number? "))
#     b = float(input("second number? "))
#     return a, b


def displayResult(x: float):
    print(f"Output: {x}", "\n")


# def performCalcLoop(calc):
#     while True:
#         choice = input("Operation? ")
#         if choice == 'q':
#             break  # user types q to quit calulator.
#         elif choice == 'add':
#             a, b = getAddNum()
#             displayResult(calc.add(a, b))
#         else:
#             print("That is not a valid input.")

def performCalcLoop(calc):
    choice = "" #Set choice to a value so it can meet the condition below and start the loop
    while choice != 8:
        choice = calcMenu()
        if choice == 1:
            print("Add")
            a, b = getAddNum()
            displayResult(calc.add(a, b))
        elif choice == 2:
            print("Subtract")
            a, b = getSubNum()
            displayResult(calc.sub(a, b))
        elif choice == 3:
            print("Multiply")
            a, b = getMultiNum()
            displayResult(calc.mul(a,b))
        elif choice == 4:
            print("Divide")
            a, b = getDivNum()
            displayResult(calc.div(a, b))
        elif choice == 5:
            print("Square")
            a, b = getSquared()
            displayResult(calc.squ(a, b))
        elif choice == 6:
            print("Square Root")
            a = getRoot()
            displayResult(calc.roo(a))
        elif choice == 7:
            print("Exponent")
            a, b = getExponent()
            displayResult(calc.exp(a, b))
        elif choice == 8:
            print("Calculator is now OFF")
        else:
            print("Invalid choice: Please enter a number between 1 - 8\n\n")

# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
