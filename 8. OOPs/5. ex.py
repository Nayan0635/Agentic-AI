class User:
    #Employee class
    #empid, empName, departments =[],salary,
    #Show 5 employees data
    #Calculate Average , Total salary of all employees.
    #Parameterized Constructor
    def __init__(self,fname:str,lname:str,age:int,gender:str,languages:list,skills:list):
        self.__fname       = fname
        self.__lname       = lname
        self.__age         = age
        self.__gender      = gender
        self.__languages   = languages
        self.__skills      = skills
   
    def getUser(self)->dict:
        return {
            "name"         :self.__fname+" "+self.__lname,
            "age"          :self.__age,
            "gender"       :self.__gender,
            "languages"    :self.__languages,
            "skills"       :self.__skills
        }
   
#MainScript
user1 = User("John","Doe",33,"Male",['Bengali','Hindi','English'],["C","C++","Python"])
user2 = User("Smith","Doe",31,"Male",languages=['Bengali','English'],skills=['C','DS','Java'])

listOfUsers = [] #Empty list
listOfUsers.append(user1.getUser())
listOfUsers.append(user2.getUser())

print(listOfUsers,len(listOfUsers))

for user in listOfUsers:
    lang = ",".join(lang for lang in user['languages'])
    skill= ",".join(skill for skill in user['skills'])
    print(user['name'],user['age'],user['gender'],lang,skill)