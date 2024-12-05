class human:
    def __init__(self):
        self.num_eyes=2
        self.num_nose=1
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")

class male(human):
    def walk(self):
        print("i can walk")
    def work(self):
        super().work()
        print("i can code") # this means override the code
male_1=male()
male_1.walk()
male_1.work()
print(male_1.num_eyes)