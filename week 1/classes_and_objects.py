class car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def start_engine(self):
        print(f"{self.color} {self.brand} engine has started! ")

car1 = car("toyoto","red")
car2 = car("tesla","black")   
car1.start_engine()
car2.start_engine()      
