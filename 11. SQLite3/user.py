class User:
    # This is a User class which will connect to Database
    def __init__(self):
        #Connection string
        # self.con = sqlite3.connect("./database/usersDB.sqlite3")
        import os
        import sqlite3

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "database", "usersDB.sqlite3")

        self.con = sqlite3.connect(db_path)
                
        
        #To access the Database we need to create cursor object.
        self.cursor = self.con.cursor()
        print("Database connected")

    def getAllUsers(self):
        self.cursor.execute("select * from users")
        users = self.cursor.fetchall()
        return users
    
    def getUser(self,uid:int):
        self.cursor.execute("select * from users where user_id=?",(uid,))
        user = self.cursor.fetchone()
        return user
    
    #Register a new user into the Database. 
    def addNewUser(self,name:str,email:str,sal:float)->str:
        self.cursor.execute("insert into users(name,email,sal)values(?,?,?)",(name,email,sal))
        
        self.con.commit()
        rows =self.cursor.rowcount
         
        if rows==1:
            return 'User successfully Registered'
        else:
            return 'Unable to add new User'
    
    #This will update the student depends on id.
    def updateUser(self,uid:int,name:str,email:str,sal:float)->str:
        user=self.getUser(uid=uid)
        if not user:
            return 'No user exists'
        else:
         if not name:
             name = user[1]
         if not email:
             email = user[2]
         if not sal:
             sal = user[3]

         self.cursor.execute('''
         update users set name=?,
                          email=?,
                          sal=?
                          where user_id=?
        ''',(name,email,sal,uid))
         self.con.commit()
         rows =self.cursor.rowcount
         if rows==1:
            return 'One User Profile successfully Updated'
         else:
            return 'Unable to Update User profile'
    
    def deleteUser(self,uid:int)->str:
        user=self.getUser(uid=uid)
        if not user:
            return 'User not exists'
        else:
         self.cursor.execute("delete from users where user_id=?",(uid,))
         self.con.commit()
         rows =self.cursor.rowcount
         if rows ==1:
            return 'Student got deleted successfully'
         else:
            return 'Unable to Delete a Student'

    def getMail(self,email):
        self.cursor.execute("select * from users where email=?",(email,))#XXX important
        user = self.cursor.fetchone()
        return user
    
    def getSalary(self):
        self.cursor.execute("SELECT * FROM users ORDER BY sal ASC")
        users = self.cursor.fetchall()
        return users
    
    # def salary(self, sal):
    #     pass