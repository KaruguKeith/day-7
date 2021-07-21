#oop is a design pattern 
#when building a complex application you need to decide the design pattern to use
#you can use a mixture of design patterns when building an application
#when building an application you need to think about scalability
#oop principles:
    #1. inheritance : ability of a child class to inherit properties from a parent class
    
class Parent:#THIS IS A PARENT CLASS
    __nationality = 'kenya' 
    def __init__(self , fname , lname):#THIS IS A CONSTRUCTOR , SELF IS REFERRING TO THE SAME OBJECT
        self.fname = fname
        self.lname = lname
    
    def printName(self):
        print(self.fname, self.lname)

class Student(Parent):#WE PASS PARENT AS A PARAMETER SO IT CAN INHERIT FROM THE PARENT CLASS
    pass
    userName = 'jadon sancho'#THIS PROPRTY IS ONLY IN STUDENT
    def doExams(self):
        print('I am sitting for a paper')

newStudent = Student('keith', 'karugu')#INSTANCE OF OUR CLASS

newStudent.printName()
newStudent.doExams()
print(newStudent.userName)
print(newStudent._nationality)