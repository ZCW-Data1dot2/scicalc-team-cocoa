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

    def sin(self, x):
        answer = math.sin(x)
        return answer

    def inverse_sin(self, x):
        answer = math.asin(x)
        return answer

    def cosine(self, x):
        answer = math.cos()
        return answer

    def inverse_cosine(self):
        answer = math.acos(x)

    def tangent(self, x):
        answer = math.tan(x)
        return answer

    def invenser_tangent(self):
        answer = math.atan(x)
        return answer