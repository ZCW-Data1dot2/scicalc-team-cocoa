import math

class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        answer = x + y
        return float(answer)

    def sub(self, x, y):
        answer = x - y
        return float(answer)

    def mul(self, x, y):
        answer = x * y
        return float(answer)

    def div(self, x, y):
        answer = x / y
        return float(answer)

    def squ(self, x):
        answer = x**x
        return float(answer)

    def roo(self, x):
        answer = math.sqrt(x)
        return float(answer)

    def exp(self,x,y):
        answer = x ** y
        return float(answer)