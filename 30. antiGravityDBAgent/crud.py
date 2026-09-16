from database import getConnection
import json
def addNewStudent(name:str,email:str)->str:
    '''adding new student to sqlite3 database'''
    (con,cursor) = getConnection()
    cursor.execute("insert into students(name,email)values(?,?)",(name,email))
    con.commit()
    rows = cursor.rowcount
    #close the Database connection
    cursor.close()
    con.close()

    if rows == 1:
        return 'One new Student added successfully'
    else:
        return 'Unble to add new Student'

def getAllStudents()->str:
    '''displaying all students from the sqlite3 database'''
    (con,cursor) = getConnection()
    cursor.execute("select * from students")
    rows=cursor.fetchall()
    students=[] #empty list
    cursor.close()
    con.close()
    for student in rows:
        students.append({
            "student_id":student[0],
            "name":student[1],
            "email":student[2]
        })
    studentJsonData = json.dumps(students,indent=1)
    return studentJsonData

def getStudent(std_id:int)->str:
    '''getting perticular student depends on student_id from sqlite3 database'''
    (con,cursor) = getConnection()
    cursor.execute("select * from students where student_id=?",(std_id,))
    row =cursor.fetchone()
    #close the datbase connection
    cursor.close()
    con.close()
    if row:
     return json.dumps({
        "student_id":row[0],
        "student_name":row[1],
        "email":row[2]
      },indent=1)
     
    else:
        return 'NO student found'