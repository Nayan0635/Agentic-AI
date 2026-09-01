from database import getConnection

def addNewStudent(name:str,email:str)->str:
    '''This function will insert a new record to Database'''
    con,cursor = getConnection()
    cursor.execute("insert into students(name,email)values(?,?)",(name,email))
    con.commit()
    rows = cursor.rowcount
    cursor.close()
    con.close()
    if rows == 1:
        return 'One Student Successfully created'
    else: 
        return 'Unable to Add a new student'
    
def getAllStudents():
    '''Getting all students from the Database'''
    con,cursor = getConnection()
    cursor.execute("select * from students")
    data =cursor.fetchall()
    students = [] #Empty list
    for row in data:
        students.append({
            'id':row[0],
            'name':row[1],
            'email':row[2]
        })
    return students
def getStudent(sid:int):
    '''getting perticular student depends on student_id pk'''
    con,cursor = getConnection()
    cursor.execute("select * from students where student_id=?",(sid,))
    student =cursor.fetchone()
    cursor.close()
    con.close()
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
    con,cursor = getConnection()
    cursor.execute("update students set name=?,email=? where student_id=?",(name,email,sid))
    con.commit()
    rows =cursor.rowcount
    cursor.close()
    con.close()
    if rows ==1:
        return {"message":"Student updated successfully"}
    else:
        return {"message":"Unable to Update Student Profile"}

def deleteStudent(sid:int):
    '''deleting student depends on student_id'''
    con,cursor = getConnection()
    cursor.execute("delete from students where student_id=?",(sid,))
    con.commit()
    rows =cursor.rowcount
    cursor.close()
    con.close()
    if rows == 1:
        return {"message":"student deleted successfully"}
    else:
        return {"message":"unable to delete a student"}
