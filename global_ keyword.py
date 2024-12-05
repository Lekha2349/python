# global keyword can be used when i want to modify global variable inside a function
x = 5  # Global variable

def my_function():
    global x
    x=10# This modifies the global variable x
    print(x) 

my_function()
print(x)  # (global variable is now changed)
