class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


a = int(input("enter the value1:"))
b = int(input("enter the value2:"))
calc = Calculator()
print("Addition: =", calc.add(a, b))
print("Subtraction: =", calc.subtract(a, b))
print("Multiplication:=", calc.multiply(a, b))
print("Division: =", calc.divide(a, b))
