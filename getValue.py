class Value:

    def getAddNum(self):
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

    def getSubNum(self):
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

    def getMultiNum(self):
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

    def getDivNum(self):
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

    def getSquared(self):
        global val_in_mem
        a = input("Enter the number that you want to square: \n")
        if a == 'mrc':
            a = float(val_in_mem)
        else:
            a = float(a)
        return a

    def getRoot(self):
        global val_in_mem
        a = input("Enter the number that you want to find the square root of : \n")
        if a == 'mrc':
            a = float(val_in_mem)
        else:
            a = float(a)
        return a

    def getExponent(self):
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