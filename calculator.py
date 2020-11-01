import math
import matplotlib as plt

class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return 0

    def factorial(self, x):
        start = 1
        for num in range(2, n + 1):
            start *= num
        return start

    def log(self, x, y):
        return math.log(x, y)
    
    def pie(self, label, slices):
        plabel = label
        pslices = slices
        plt.pie(pslices, labels=plabel,
                startangle=90, shadow=True, explode=(0, 0, 0.1, 0),
                radius=1.5, autopct='%1.2f%%')


# add lots more methods to this calculator class.
