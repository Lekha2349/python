# local variable means accessed within the function
def my_function():
    local_var = 10  # local_var is local to my_function
    print(local_var)

my_function() 
# print(local_var)  # This would cause an error because local_var is not accessible outside my_function
