from user import User
import os
print(os.getcwd())
if __name__=="__main__":
 while True:  
    print("1.View all Users")
    print("2. Show Specific user by id :")
    print("5. Register new User")
    print("6. Update an User")
    print("7. Delete an User")
    print("8. Exit")
    #Create an Object of the User class
    user1 = User()
    choice = int(input("Enter Your choice between 1-5: "))
    
    if choice == 1:
        users =user1.getAllUsers()
        for user in users:
            print(user[0],user[1],user[2],user[3])
       
    elif choice==2:
       uid = int(input("Enter User id:"))
       user=user1.getUser(uid)
       if not user:
          print("No Users found!")
       else:
          print(user[1],user[2],user[3])
   
    elif choice==3:
       email = input("Enter User email:")
       user = user1.getMail(email)
       if not user:
          print("No Users found with that mail!")
       else:
          print(user[1],user[2],user[3]) 
    
    elif choice == 4:
      users = user1.getSalary()
      for user in users:
         print(user) 
         
    elif choice == 5:
       newName = input("Enter Name:")
       newEmail= input("Enter email")
       newSal  = float(input("Salary:"))
       print(user1.addNewUser(name=newName,email=newEmail,sal=newSal))

    elif choice == 6:
       newName = input("Enter Name:")
       newEmail= input("Enter email")
       newSal  = input("Salary:")
       uid     = int(input("Enter user id:"))
       print(user1.updateUser(name=newName,email=newEmail,sal=newSal,uid=uid))

    elif choice ==7:
       uid = int(input("Enter user id:"))
       print(user1.deleteUser(uid=uid))
      
    elif choice==8:
        #XXX Database Connection has to be closed .    
        user1.cursor.close()
        user1.con.close()
        print("Bye Bye")
        exit(0)