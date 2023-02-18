class DivideByZeroError(Exception):
    pass

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            raise DivideByZeroError("Cannot divide by zero")
        return result

calc = Calculator()
try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(calc.add(x, y))
    print(calc.subtract(x, y))
    print(calc.multiply(x, y))
    print(calc.divide(x, y))
except ValueError:
    print("Invalid input")
except DivideByZeroError as e:
    print(e)
