#
class shapes():
    #abstractmethod

    def calculatePerimeter(self):
        pass

class Triangle(shapes):
    #overiding abstract

    def calculatePerimeter(self):
        print('I have 3 sides')
    
class Quadrilateral(shapes):
    #overiding abstract method
    def calculatePerimeter(self,height):
        p=height*4

#drivercode
R = Quadrilateral()
perimeter = R.calculatePerimeter(40)
print(perimeter)