class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Creating a Calculator object
calc = Calculator()

# Testing the add method with different numbers of arguments
print("Adding two numbers:", calc.add(2, 3))       # Output: 5
print("Adding three numbers:", calc.add(2, 3, 4))  # Output: 9
