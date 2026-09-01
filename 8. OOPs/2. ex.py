class User:
   
    def setValues(self,fname:str,lname:str,age:int,gender:str):
        self.__fname = fname
        self.__lname = lname
        self.__age   = age
        self.__gender= gender

    def getValues(self)->dict:
        return {
            "name":self.__fname+" "+self.__lname,
            "age" : self.__age,
            "gender":self.__gender
        }  

user1 = User()
user1.setValues("John","Doe",31,"Male")
user2 = User()
user2.setValues("Diana","Doe",33,"Female")


listOfUsers = [] #Empty list
listOfUsers.append(user1.getValues())
listOfUsers.append(user2.getValues())
#Displaying entire users
for user in listOfUsers:
    print(user['name'],user['age'],user['gender'])