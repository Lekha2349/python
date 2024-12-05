class Animal:

    def __init__(self,legs,is_veg,weight) -> None:
        self.number_of_legsnumber_of_legs = legs # integer
        self.is_vegetarian = is_veg # bool
        self.weight = weight # float
    def sounds(self):
        print( "makes bow bow... sound")
    def show_weight(self):
        print("Weight of dog is "+ str(self.weight))
if __name__ == "__main__":
    dog = Animal(legs=4,weight=50.5,is_veg=False)
    dog.sounds()
    dog.show_weight()    


