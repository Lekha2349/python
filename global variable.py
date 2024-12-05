# Variables that are defined outside any function or class and are accessible from anywhere in the code.
global_var = 40  # global_var is a global variable

def my_function():
    print(global_var)  # Accessing the global variable

my_function()  
print(global_var)  
