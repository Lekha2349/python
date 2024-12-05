# Certainly! In hierarchical inheritance, you have a single superclass (parent class) that serves as the base for multiple subclasses (child classes). Each subclass inherits all the properties and behaviors of the superclass, but can also have its own unique properties and behaviors.

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")


dog_instance = Dog()
cat_instance = Cat()


dog_instance.speak()  
dog_instance.bark()   

cat_instance.speak()  
cat_instance.meow()   
