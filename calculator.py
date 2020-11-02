import math

class Calculator:

    def __init__(self):
        pass

    def add(self, x, y, disp_mode):
        answer = (x+y)
        int_answer = int(answer)
        if disp_mode == 'binary':
            return bin(int_answer)
        elif disp_mode == 'hexadecimal':
            return hex(int_answer)
        elif disp_mode == 'octal':
            return oct(int_answer)
        elif disp_mode == 'decimal':
            return float(answer)

    # def add(self, x, y):
    #     return x + y

    def sub(self, x, y, disp_mode):
        answer = (x-y)
        int_answer = int(answer)
        if disp_mode == 'binary':
            return bin(int_answer)
        elif disp_mode == 'hexadecimal':
            return hex(int_answer)
        elif disp_mode == 'octal':
            return oct(int_answer)
        elif disp_mode == 'decimal':
            return float(answer)
    def mul(self, x, y, disp_mode):
        answer = (x * y)
        int_answer = int(answer)
        if disp_mode == 'binary':
            return bin(int_answer)
        elif disp_mode == 'hexadecimal':
            return hex(int_answer)
        elif disp_mode == 'octal':
            return oct(int_answer)
        elif disp_mode == 'decimal':
            return answer

    def div(self, x, y, disp_mode):
        answer = (x / y)
        int_answer = int(answer)
        if disp_mode == 'binary':
            return bin(int_answer)
        elif disp_mode == 'hexadecimal':
            return hex(int_answer)
        elif disp_mode == 'octal':
            return oct(int_answer)
        elif disp_mode == 'decimal':
            return answer

    def squ(self, x, disp_mode):
        answer = (x ** x)
        int_answer = int(answer)
        if disp_mode == 'binary':
            return bin(int_answer)
        elif disp_mode == 'hexadecimal':
            return hex(int_answer)
        elif disp_mode == 'octal':
            return oct(int_answer)
        elif disp_mode == 'decimal':
            return answer

    def roo(self, x, disp_mode):
        answer = math.sqrt(x)
        int_answer = int(answer)
        if disp_mode == 'binary':
            return bin(int_answer)
        elif disp_mode == 'hexadecimal':
            return hex(int_answer)
        elif disp_mode == 'octal':
            return oct(int_answer)
        elif disp_mode == 'decimal':
            return float(answer)

    def exp(self, x, y, disp_mode):
        answer = (x ** y)
        int_answer = int(answer)
        if disp_mode == 'binary':
            return bin(int_answer)
        elif disp_mode == 'hexadecimal':
            return hex(int_answer)
        elif disp_mode == 'octal':
            return oct(int_answer)
        elif disp_mode == 'decimal':
            return answer

