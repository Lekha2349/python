# Arrays in Python are like containers that hold multiple pieces of data, all of the same type, like numbers or words

#  They're organized in a sequence, which means you can access each piece of data using its position or index in the array. Think of it like a row of boxes, each containing something different

# You can easily add or remove items from the array, and perform operations on all the items at once. It's a convenient way to handle lots of related data together!

# Creating an array of numbers
numbers = [1, 2, 3, 4, 5]

# Accessing elements in the array
print("First number:", numbers[0])
print("Second number:", numbers[1])

# Adding a new number
numbers.append(6)
print("After adding a new number:", numbers)

# Removing a number
removed_number = numbers.pop(2)  # Removing the number at index 2
print("Removed number:", removed_number)
print("Remaining numbers:", numbers)
# buffer_function()) it will give address of the function
# type code will give which datatype