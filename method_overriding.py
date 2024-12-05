class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Creating objects
animal = Animal()
dog = Dog()

# Method calls
animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Dog barks
