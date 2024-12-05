# Using Regular Methods (Getters and Setters)
# Create the Class with a Constructor:
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
# Add Getter Methods:
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
# Add Setter Methods:
    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            raise ValueError("Age cannot be negative")
# using python methods also we can use

