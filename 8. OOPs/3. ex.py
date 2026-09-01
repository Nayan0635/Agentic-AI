class User:
   
    def setValues(self,fname:str,lname:str,age:int,gender:str, language:list, skills:list):
        self.__fname = fname
        self.__lname = lname
        self.__age   = age
        self.__gender= gender
        self.__language= language
        self.__skills= skills

    def getValues(self)->dict:
        return {
            "name":self.__fname+" "+self.__lname,
            "age" : self.__age,
            "gender":self.__gender,
            "language":self.__language,
            "skills":self.__skills
        }  

user1 = User()
user1.setValues("John","Doe",31,"Male", ["Hindi", "Spanish", "English"],["C++", "Python"])
user2 = User()
user2.setValues("Diana","Doe",33,"Female", ["Hindi", "Bengali", "English"],["C++", "Python", "TypeScript"])


listOfUsers = [] #Empty list
listOfUsers.append(user1.getValues())
listOfUsers.append(user2.getValues())
#Displaying entire users
for user in listOfUsers:
    print(user['name'],user['age'],user['gender'], user["language"], user['skills'], end="\n")