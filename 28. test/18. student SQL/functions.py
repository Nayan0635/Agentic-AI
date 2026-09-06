from langchain_core.tools import tool
from connection import getConnection, closeConnection
import json


@tool
def showAll():
    '''Show all student records from the database.'''
    con, cur = getConnection()
    cur.execute("select * from students")
    
    info = cur.fetchall()
    students = []
    
    for st in info:
        students.append({
            "id": st[0],
            "name": st[1],
            "email": st[2],
            "course": st[3]
        })
        
    closeConnection(con, cur)
    return json.dumps(students, indent=1)

@tool
def findOne(id: int):
    '''Find student data with specific student_id.'''
    con, cur = getConnection()
    
    cur.execute("select * from students where student_id = ?", (id,))
    row = cur.fetchone()
    closeConnection(con, cur)
    
    if row:
        return {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "course": row[3],
        }
    else:
        return "Didn't find anyone with that id."

@tool
def addNew(name: str, email: str, course: str):
    '''Add new student information into the database.'''
    con, cur = getConnection()
    cur.execute("insert into students(name, email, course) values(?, ?, ?)", (name, email, course))
    con.commit()
    rows = cur.rowcount
    closeConnection(con, cur)
    
    if rows == 1:
        return "added new student successfully."
    else:
        return "unable to add student."

@tool
def update(id: int, name: str = None, email: str = None, course: str = None):
    '''Update an existing student's name, email, or course.
    Use this tool when the user asks to update, change, modify,
    or edit an existing student's information.
    Requires the student's student_id (id).'''
    con, cur = getConnection()
    
    cur.execute("select * from students where student_id = ?", (id,))
    student = cur.fetchone()
    
    if not student:
        closeConnection(con, cur)
        return "student doesn't exist."
    
    if not name:
        name = student[1]
    if not email:
        email = student[2]
    if not course:
        course = student[3]
    cur.execute("update students set name = ?, email = ?, course = ? where student_id = ?", (name, email, course, id))
    con.commit()
    rows = cur.rowcount
    closeConnection(con, cur)
    
    if rows == 1:
        return "student profile successfully updated."
    else:
        return "unable to update student."

@tool
def delete(id: int):
    '''Delete a student record from the database by student id.'''
    con, cur = getConnection()
    cur.execute("delete from students where student_id = ?", (id,))
    con.commit()
    rows = cur.rowcount
    closeConnection(con, cur)
    
    if rows == 1:
        return "deleted student successfully."
    else:
        return "unable to delete student."