#getters and setters dont care about encapsulation
#these are functions awhich are defined by the developer

class User:
    def __init__(self , userName , email , password):
        self.userName = userName
        self.email = email
        self.password = password
    
    def getuserName (self):
        return self.userName

    def setuserName(self , userName):
        self.userName = userName

class Student(User):
    pass

newUser = Student('keith' , 'karugukeith@gmail.com' , '12334456')
newUser.setuserName('karugu')

print(newUser.getuserName)