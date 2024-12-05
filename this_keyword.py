# self is used inside a class to refer to the instance of the class. It's the way to access instance variables and methods from within the class.

class Person:
    def __init__(self, name):
        self.name = name  # 'self' refers to the current instance

    def print_name(self):
        print(self.name)  # 'self' refers to the current instance

person = Person("Alice")
person.print_name()  # Output: Alice
