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
            'name':row[1],
            'email':row[2]
        })
    return students
