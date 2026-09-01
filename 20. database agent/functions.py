from connect import *
import json

# tool 1
def showAll():
    '''SHOW all records from database'''
    (con, cur) = getConnection()
    cur.execute("SELECT * FROM students")
    
    data = cur.fetchall()
    students = []
    
    for st in data:
        students.append({
            "id" : st[0],
            "name" : st[1],
            "email" : st[2]
        })
        
    closeConnection(con, cur)
    return json.dumps(students, indent=1)

# tool 2
def addNew(name, email):
    '''add a new student'''
    (con, cur) = getConnection()
    cur.execute("INSERT INTO students(name, email)values(?,?)",(name, email))
    con.commit()
    rows = cur.rowcount
    closeConnection(con, cur)
    
    if rows == 1:
        return 'Added student to the database.'
    else:
        return 'Unable to add student.'
    
# tool 3
def update(id, name, email):
    '''upadting existing student details'''
    (con,cur) = getConnection()
    
    cur.execute("select * from students where student_id= ?", (id,))
    student = cur.fetchone()
    if not student:
        closeConnection(con, cur)
        return 'student not found.'
    
    if not name:
        name = student[1]
    if not email:
        email = student[2]
    cur.execute("UPDATE students SET name=?, email=? WHERE student_id=?",(name, email, id))
    con.commit()
    rows = cur.rowcount
    closeConnection(con, cur)
    
    if rows == 1:
        return 'Updated student successfully.'
    else:
        return 'Unable to update student.'

# tool 4
def delete(id):
    '''delete exisiting student data'''
    (con,cur) = getConnection()
    cur.execute("DELETE FROM students where student_id=?",(id,))
    con.commit()
    rows = cur.rowcount
    closeConnection(con, cur)
    
    if rows == 1:
        return 'Deleted student from database.'
    else:
        return 'Unable to delete student.'
    