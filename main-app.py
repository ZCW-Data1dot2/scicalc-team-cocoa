#import matplotlib.pyplot as plt
from calculator import Calculator
from getValue import Value


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

def display(int_answer, disp_mode):
    if disp_mode == 'binary':
        return bin(int_answer)
    elif disp_mode == 'hexadecimal':
        return hex(int_answer)
    elif disp_mode == 'octal':
        return oct(int_answer)
    elif disp_mode == 'decimal':
        return float(int_answer)
    else:
        return float(int_answer)

def switchDisplayMode(user_choice, prev_mode):
    global display_modes
    if user_choice == 'default':
        disp_mode = display_modes[prev_mode]
    else:
        disp_mode = user_choice
    return disp_mode


def displayResult(x: float):
    print(f"Output: {x}", "\n")



def performCalcLoop(calc):
    global val_in_mem
    value = Value()
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
            a, b = value.getAddNum()
            result = calc.add(a, b)
            dResult = display(result, disp_inpt)
            displayResult(dResult)
        elif choice == 2:
            print("Subtract")
            a, b = value.getSubNum()
            result = calc.sub(a, b)
            dResult = display(result, disp_inpt)
            displayResult(dResult)
        elif choice == 3:
            print("Multiply")
            a, b = value.getMultiNum()
            result = calc.mul(a, b)
            dResult = display(result, disp_inpt)
            displayResult(dResult)
        elif choice == 4:
            print("Divide")
            a, b = value.getDivNum()
            result = calc.div(a,b)
            if result == int:
                dResult = display(result, disp_inpt)
                displayResult(dResult)
            else:
                print("Err")
        elif choice == 5:
            print("Square")
            a = value.getSquared()
            result = calc.squ(a)
            dResult = display(result, disp_inpt)
            displayResult(dResult)
        elif choice == 6:
            print("Square Root")
            a = value.getRoot()
            result = calc.roo(a)
            dResult = display(result, disp_inpt)
            displayResult(dResult)
        elif choice == 7:
            print("Exponent")
            a, b = value.getExponent()
            result = calc.exp(a, b)
            displayResult(result)
        elif choice == 8:
            print("Calculator is now OFF")
            #sys.exit(0)
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
    value = Value()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
