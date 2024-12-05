# Exception handling in Python is a way to manage errors that occur during the execution of a program. When an error happens, instead of stopping the entire program, Python allows you to catch and handle these errors, so the program can continue to run or fail gracefully

try:
    # Code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    # Code to run if a ZeroDivisionError occurs
    print("You can't divide by zero!")
else:
    # Code to run if no error occurs in try block
    print("The division was successful.")
finally:
    # Code to run no matter what
    print("This will always execute.")
