# Update a Value
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Update the value of an existing key
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

# Delete a Key-Value Pair
my_dict = {
    "name": "Alice",
    "age": 31,
    "city": "New York"
}

# Delete a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31}

#  pop() method:
my_dict = {
    "name": "Alice",
    "age": 31,
    "city": "New York"
}

# Delete a key-value pair and get its value
city = my_dict.pop("city")
print(city)     # Output: New York
print(my_dict)  # Output: {'name': 'Alice', 'age': 31}


