#import matplotlib.pyplot as plt

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
    8) PIE TIME
    9) EXIT
    """)
    choice = int(input("PLEASE ENTER A NUMBER BETWEEN 1 - 9: \n"))
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
    if user_choice == 'default':
        disp_mode = display_modes[prev_mode]
    else:
        disp_mode = user_choice
    return disp_mode


def pie(label, slices):
    plabel = label
    pslices = slices
    plt.pie(pslices, labels=plabel, startangle=90, shadow=True, explode=(0, 0, 0.1, 0), radius=1.5,
            autopct='%1.2f%%')
    plt.pyplot.legend()
    plt.pyplot.show()

def displayResult(x: float):
    print(f"Output: {x}", "\n")

def performCalcLoop(calc):
    global val_in_mem
    subject_list = []
    percent_list = []
    disp_prev_num = 0
    disp_ask = input("Set a display mode?\n")
    if disp_ask == '' or disp_ask == 'n':
        disp_inpt = 'default'
    elif disp_ask == 'y':
        disp_inpt = input("Which mode" + str(display_modes))
    choice = ""  # Set choice to a value so it can meet the condition below and start the loop
    while choice != 9:
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
            displayResult(calc.sub(a, b, disp_mode))
        elif choice == 3:
            print("Multiply")
            a, b = getMultiNum()
            displayResult(calc.mul(a, b, disp_mode))
        elif choice == 4:
            print("Divide")
            a, b = getDivNum()
            displayResult(calc.div(a, b, disp_mode))
        elif choice == 5:
            print("Square")
            a, b = getSquared()
            displayResult(calc.squ(a, disp_mode))
        elif choice == 6:
            print("Square Root")
            a = getRoot()
            displayResult(calc.roo(a, disp_mode))
        elif choice == 7:
            print("Exponent")
            a, b = getExponent()
            displayResult(calc.exp(a, b, disp_mode))
        elif choice == 9:
            print("Calculator is now OFF")
        # elif choice == 8:
        #     print("Lets make a pie chart!")
        #     subcount = int(input("How many subjects are on your pie chart?\n"))
        #     for x in range(0, subcount):
        #         sub = str(input("Please enter your subject\n"))
        #         subject_list.append(sub)
        #
        #     # percentage = input(input("How much of each on your pie?\n"))
        #     for x in range(0, subcount):
        #         percent = input("Please enter the percentage for each subject\n")
        #         percent_list.append(percent)
        #     print("Please wait....creating pie")
        #     pie(subject_list, percent_list)
        else:
            print("Invalid choice: Please enter a number between 1 - 9\n\n")
        disp_prev_num += 1
        user_inpt = input()
        if user_inpt == 'm+':
            val_in_mem = result
            print(result)
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
