from connection import *

def addNewStudent(name:str,email:str)->str:
    '''This function will insert a new record to Database'''
    con,cur = getConnection()
    cur.execute("insert into students(name,email)values(?,?)",(name,email))
    con.commit()
    rows = cur.rowcount
    closeConnection(con, cur)
    if rows == 1:
        return 'One Student Successfully created'
    else: 
        return 'Unable to Add a new student'
    
def getAllStudents():
    '''Getting all students from the Database'''
    con,cur = getConnection()
    cur.execute("select * from students")
    data =cur.fetchall()
    students = [] #Empty list
    for row in data:
        students.append({
            'id':row[0],
            'name':row[1],
            'email':row[2]
        })
    closeConnection(cur, con)
    return students
def getStudent(sid:int):
    '''getting perticular student depends on student_id pk'''
    con,cur = getConnection()
    cur.execute("select * from students where student_id=?",(sid,))
    student =cur.fetchone()
    closeConnection(con, cur)
    if student:
     student = {
        "name":student[1],
        "email":student[2]
     }
    else:
        return {"message":"No student found"} 
    
    return student

def updateStudent(sid:int,name:str,email:str):
    student:dict = getStudent(sid)
    if not name:
        name = student.get("name")
    if not email:
        email = student.get("email")
    con,cur = getConnection()
    cur.execute("update students set name=?,email=? where student_id=?",(name,email,sid))
    con.commit()
    rows =cur.rowcount
    closeConnection(con, cur)
    if rows ==1:
        return {"message":"Student updated successfully"}
    else:
        return {"message":"Unable to Update Student Profile"}

def deleteStudent(sid:int):
    '''deleting student depends on student_id'''
    con,cur = getConnection()
    cur.execute("delete from students where student_id=?",(sid,))
    con.commit()
    rows =cur.rowcount
    closeConnection(con, cur)
    if rows == 1:
        return {"message":"student deleted successfully"}
    else:
        return {"message":"unable to delete a student"}
