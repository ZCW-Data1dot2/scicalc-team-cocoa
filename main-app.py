from calculator import Calculator
display_modes = ['decimal', 'binary', 'octal', 'hexadecimal']
val_in_mem = 0
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
    global val_in_mem
    a = input("Enter the first number that you want to add: \n")
    if a == 'mrc':
        a = float(val_in_mem)
    else:
        a = float(a)
    b = input("Enter the second number that you want to add: \n")
    if b == 'mrc':
        b = float(val_in_mem)
    else:
        b = float(b)

    return a, b

def getSubNum():
    global val_in_mem
    a = input("Enter the first number that you want to subtract: \n")
    if a == 'mrc':
        a = float(val_in_mem)
    else:
        a = float(a)
    b = input("Enter the second number that you want to subtract: \n")
    if b == 'mrc':
        b = float(val_in_mem)
    else:
        b = float(b)
    return a, b

def getMultiNum():
    global val_in_mem
    a = input("Enter the first number that you want to multiply: \n")
    if a == 'mrc':
        a = float(val_in_mem)
    else:
        a = float(a)
    b = input("Enter the second number that you want to multiply: \n")
    if b == 'mrc':
        b = float(val_in_mem)
    else:
        b = float(b)
    return a, b

def getDivNum():
    global val_in_mem
    a = input("Enter the first number that you want to divide: \n")
    if a == 'mrc':
        a = float(val_in_mem)
    else:
        a = float(a)
    b = input("Enter the second number that you want to divide: \n")
    if b == 'mrc':
        b = float(val_in_mem)
    else:
        b = float(b)
    return a, b

def getSquared():
    global val_in_mem
    a = input("Enter the number that you want to square: \n")
    if a == 'mrc':
        a = float(val_in_mem)
    else:
        a = float(a)
    return a

def getRoot():
    global val_in_mem
    a = input("Enter the number that you want to find the square root of : \n")
    if a == 'mrc':
        a = float(val_in_mem)
    else:
        a = float(a)
    return a

def getExponent():
    global val_in_mem
    a = input("Enter the base number : \n")
    if a == 'mrc':
        a = float(val_in_mem)
    else:
        a = float(a)
    b = input("Enter the exponent number : \n")
    if b == 'mrc':
        b = float(val_in_mem)
    else:
        b = float(b)
    return a, b

def switchDisplayMode(user_choice, prev_mode):
    global display_modes
    if user_choice == 'default':
        disp_mode = display_modes[prev_mode]
    else:
        disp_mode = user_choice
    return disp_mode


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
    global val_in_mem
    disp_prev_num = 0
    disp_ask = input("Set a display mode? y or n\n")
    if disp_ask == '' or disp_ask == 'n':
        disp_inpt = 'default'
    elif disp_ask == 'y':
        disp_inpt = input("Which mode\n" + str(display_modes) + '\n')
    choice = "" #Set choice to a value so it can meet the condition below and start the loop
    while choice != 8:
        if disp_prev_num > 3:
            disp_prev_num = 0
        disp_mode = switchDisplayMode(disp_inpt, disp_prev_num)
        choice = calcMenu()
        if choice == 1:
            print("Add")
            a, b = getAddNum()
            result = calc.add(a, b, disp_mode)
            displayResult(result)
        elif choice == 2:
            print("Subtract")
            a, b = getSubNum()
            result = calc.sub(a, b, disp_mode)
            displayResult(result)
        elif choice == 3:
            print("Multiply")
            a, b = getMultiNum()
            result = calc.mul(a, b, disp_mode)
            displayResult(result)
        elif choice == 4:
            print("Divide")
            a, b = getDivNum()
            result = calc.div(a, b, disp_mode)
            displayResult(result)
        elif choice == 5:
            print("Square")
            a = getSquared()
            result = calc.squ(a, disp_mode)
            displayResult(result)
        elif choice == 6:
            print("Square Root")
            a = getRoot()
            result = calc.roo(a, disp_mode)
            displayResult(result)
        elif choice == 7:
            print("Exponent")
            a, b = getExponent()
            result = calc.exp(a, b, disp_mode)
            displayResult(result)
        elif choice == 8:
            print("Calculator is now OFF")
        else:
            print("Invalid choice: Please enter a number between 1 - 8\n")
        disp_prev_num += 1
        user_inpt = input()
        if user_inpt == 'm+':
            if disp_mode == 'octal':
                val_in_mem = int(result,8)
            elif disp_mode == 'binary':
                val_in_mem = int(result,2)
            elif disp_mode == 'hexadecimal':
                val_in_mem = int(result,16)
            elif disp_mode == 'decimal':
                val_in_mem = result
        print(val_in_mem)
        if user_inpt == 'mc':
            val_in_mem = 0
# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()


# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
