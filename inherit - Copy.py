from abc import ABC,abstractmethod
class Person():
    cityName = "mumbai"
    def printName(self,name):
        print(name)
class Ashok:
    def printDetails(self):
        print("some msg")
class gowda:
    def printDetails(self):
        print("some msg")
obj = Ashok()
obj.cityName = "banglore"
obj.printName("Ashok")
obj.printDetails()
obj1 = gowda()
obj1.cityName = "london"
obj1.printName("gowda")
obj1.printDetails()