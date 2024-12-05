# Multilevel inheritance is a type of inheritance where a class is derived from another class, which in turn is derived from another class. This creates a chain of inheritance.
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Labrador(Dog):
    def fetch(self):
        print("Labrador fetches")


labrador_instance = Labrador()


labrador_instance.speak()   
labrador_instance.bark()    
labrador_instance.fetch()   

