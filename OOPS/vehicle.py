
class Vehicle:
    def __init__(self,color):
        self.color = color
    
    moves = True

class Bus(Vehicle):
    pass
   

busObj = Bus("white")
print(busObj.moves)
print(busObj.color)