# Definition: A class method is a method that is bound to the class and not the instance of the class. It can modify class state that applies across all instances of the class.
# How to Define and Use a Class Method
# 1.Decorator: Use @classmethod to define a class method.
# 2.First Parameter: The first parameter must be cls, which refers to the class itself.
class Dog: # class
    total_dogs = 0  # Class variable to track the total number of dogs

    def __init__(self, name):
        self.name = name
        Dog.total_dogs += 1  # Incrementing total_dogs when a new dog is created

    @classmethod
    def get_total_dogs(cls):
        return cls.total_dogs

# Creating instances of Dog
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# Accessing class method using the class itself
print(Dog.get_total_dogs())  # Outputs: 2
