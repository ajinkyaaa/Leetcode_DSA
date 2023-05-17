
from abc import ABC,abstractclassmethod
from typing import final


class College(ABC):

    def __init__(self,name,location,availableCourses):
        self.collegeName = name
        self.loc = location
        self.courseList = availableCourses
        self.__secret = "this is secret"
        self._protected = "this is protected"

    
    def display(self)-> None:
        print("College name is {}".format(self.collegeName))
        print("College name is {}".format(self.loc))
        print("displaying secret of College {}".format(self.__secret))

    @abstractclassmethod
    def getCourses(self):
        pass
    
    @abstractclassmethod
    def add(self,a,b):
        pass

class Sports():
    def __init__(self,team):
        self.team = team

class Student(College,Sports):
    def __init__(self,name,age,courses):
        self.name = name
        self.age  = age
        self._studSecret = "this is student secret"
        College.__init__(self,"college A","Thane",[1,2,3,4])
        Sports.__init__(self,"Team A")
    
    classVar = "this is class variable"
    def display(self) -> None:
        print("Student name is {}".format(self.name))
        print("show parent _protected {}".format(self._protected))

    def getCourses(self):
        print("courses are {}".format(self.courseList))
        
    def add(self,a,b):
        print(a+b)
        return a+b

    def add(self,a,b,c):
        print(a+b+c)
        return a+b+c

    def showSecret(self):
        print(self.__secret)

    def showTeam(self):
        print(self.team)

    def getClassVariables(cls):
        print("class Variables ",cls.classVar)
    
    

c = Student("abc","Thane",[1,2,3])
c.display()
c.getCourses()
print("c._protected" ,c._protected)
print(c.showTeam())
#print("add ",c.add(2,3,5))
#print(c.showSecret())
c.getClassVariables()


