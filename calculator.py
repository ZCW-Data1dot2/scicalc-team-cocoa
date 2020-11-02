import math
#import matplotlib.pyplot


class Calculator:

    def __init__(self):
        pass

    def add(self, x, y, disp_mode):
        answer = int(x + y)
        if disp_mode == 'binary':
            return bin(answer)
        elif disp_mode == 'hexadecimal':
            return hex(answer)
        elif disp_mode == 'octal':
            return oct(answer)
        elif disp_mode == 'decimal':
            return answer

    # def add(self, x, y):
    #     return x + y

    def sub(self, x, y, disp_mode):
        answer = int(x - y)
        if disp_mode == 'binary':
            return bin(answer)
        elif disp_mode == 'hexadecimal':
            return hex(answer)
        elif disp_mode == 'octal':
            return oct(answer)
        elif disp_mode == 'decimal':
            return answer

    def mul(self, x, y, disp_mode):
        answer = int(x * y)
        if disp_mode == 'binary':
            return bin(answer)
        elif disp_mode == 'hexadecimal':
            return hex(answer)
        elif disp_mode == 'octal':
            return oct(answer)
        elif disp_mode == 'decimal':
            return answer

    def div(self, x, y, disp_mode):
        answer = int(x / y)
        if disp_mode == 'binary':
            return bin(answer)
        elif disp_mode == 'hexadecimal':
            return hex(answer)
        elif disp_mode == 'octal':
            return oct(answer)
        elif disp_mode == 'decimal':
            return answer

    def squ(self, x, disp_mode):
        answer = int(x ** x)
        if disp_mode == 'binary':
            return bin(answer)
        elif disp_mode == 'hexadecimal':
            return hex(answer)
        elif disp_mode == 'octal':
            return oct(answer)
        elif disp_mode == 'decimal':
            return answer

    def roo(self, x, disp_mode):
        answer = int(math.sqrt(x))
        if disp_mode == 'binary':
            return bin(answer)
        elif disp_mode == 'hexadecimal':
            return hex(answer)
        elif disp_mode == 'octal':
            return oct(answer)
        elif disp_mode == 'decimal':
            return answer

    def exp(self, x, y, disp_mode):
        answer = int(x ** y)
        if disp_mode == 'binary':
            return bin(answer)
        elif disp_mode == 'hexadecimal':
            return hex(answer)
        elif disp_mode == 'octal':
            return oct(answer)
        elif disp_mode == 'decimal':
            return answer

    def log(self, x, y):
        return math.log(x, y)

    def pie(self, label, slices):
        plabel = label
        pslices = slices
        matplotlib.pyplot.pie(pslices, labels=plabel, startangle=90, shadow=True, explode=(0, 0, 0.1, 0), radius=1.5,
                              autopct='%1.2f%%')
