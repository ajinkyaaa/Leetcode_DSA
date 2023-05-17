
from abc import ABC,abstractclassmethod

class Animals(ABC):
    @abstractclassmethod
    def properties(self):
        pass

class Lion(Animals):
    def __init__(self):
        pass
    
    def properties(self):
        print("I am Lion")
        return "ABC"

        
        

l = Lion()
print(l.properties())