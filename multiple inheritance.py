class Parent1:
    def greet(self):
        print("Hello from Parent1")

class Parent2:
    def farewell(self):
        print("Goodbye from Parent2")

class Child(Parent1, Parent2):
    pass


child_instance = Child()

child_instance.greet()     
child_instance.farewell()   

