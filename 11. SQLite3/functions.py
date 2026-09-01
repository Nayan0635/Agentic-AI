import sqlite3
class MyClass:
    def __init__(self):
        self.con = sqlite3.connect("./database/userData.sqlite3")

        # self is the current object.
        # self.con means a variable named 'con' is stored inside this object.
        # 'con' is just a variable name. You could name it banana, db, x, etc.
        # By convention, we use 'con' because it stands for Connection.

        # IMPORTANT:
        # self.con does NOT store the database file path.
        # It stores the Connection object returned by connect().
        # That Connection object knows how to communicate with
        # usersData.sqlite3.
        self.cursor = self.con.cursor()
        # cursor() is a method of the Connection object.
        # It returns a Cursor object, which is used to execute SQL queries.
        print("DataBase Connected")

    def getEmployees(self):
        self.cursor.execute("select * from Employee")
        #After execute(), the query has run, but the data is still inside the cursor.
        all_employees = self.cursor.fetchall()
        return all_employees
    
    def findEmployee(self, e_id):
        self.cursor.execute("select * from Employee where emp_id = ?",(e_id,)) #esecute(Query, touple/list)
        emp = self.cursor.fetchone()
        return emp
        
    def addEmployee(self, nm, mail, s):
        self.cursor.execute("insert into Employee(name, email, sal)values(?,?,?)",(nm, mail, s))
        # the data is not permanently saved to the database yet. 
        # It is only part of the current transaction.
        # commit() tells SQLite:"Save all the changes permanently."
        self.con.commit()
        rows = self.cursor.rowcount
        #rowcount tells you how many rows were affected by the last SQL statement.
        
        if rows == 1:
            return "Employee successfully registered."
        else:
            return "Unable to add user."
            
    def updateEmp(self, id, name, mail, salary):
        emp = self.findEmployee(id)
        if not emp:
            return "No employee found"
        else:
            if not name:
                name = emp[1]
            if not mail:
                mail = emp[2]
            if not salary:
                salary = emp[3]
        self.cursor.execute('''
        update Employee set name = ?,
                            email = ?,
                            sal = ?
                            where emp_id = ?
        ''',(name, mail, salary, id))
        self.con.commit()
        if self.cursor.rowcount == 1:
            return "employee profile succesfully updated"
        else:
            return "unable to update profile"
        
    def deleteEmployee(self, id):
        emp = self.findEmployee(id)
        if not emp:
            return "No employee found"
        else:
            self.cursor.execute("delete from Employee where emp_id = ?",(id,))
            self.con.commit()
            rows = self.cursor.rowcount
            if rows == 1:
                return "Employee got fired"
            else:
                return "unable to delete Employee"
            
    def salary(self):
        self.cursor.execute("select * from Employee order by sal ASC")
        emps = self.cursor.fetchall()
        return emps