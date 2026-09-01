from langchain_core.tools import tool
from connection import *
import json


@tool
def addNew(name, email, address, course):
    '''adding a new student including their course and enrollment'''
    (con, cur) = getConnection()
    
    try:#students table
        cur.execute('''insert or ignore into students(name, email, address)
            values (?, ?, ?)''', (name, email, address))
        
        cur.execute("select student_id from students where email = ?", (email, ))
        student = cur.fetchone()
        if not student: #input violating rules...
            return "Unable to add student."
        student_id = student[0]# --> get student_id
        
        # courses table
        cur.execute('''insert or ignore into courses(course_name)
        values (?)''', (course, ))
        
        cur.execute("select course_id from courses where course_name = ?", (course, ))
        course_data = cur.fetchone()
        if not course_data:
            return 'Unable to add course'
        course_id = course_data[0]#--> get course_id
        
        # add with enrollments table
        cur.execute('''insert or ignore into enrollments(student_id, course_id)
        values (?, ?)''', (student_id, course_id))
        
        con.commit()
        return 'Added student successfully'
        
    except Exception as e:
        con.rollback()
        return f'Unable to add student: {e}'
    finally:
        closeConnection(con, cur)


@tool
def showOne(sid):
    '''Get/view/read the details of one existing student.
    Use this tool ONLY when the user wants to see student information.
    Do NOT use this tool when the user wants to change or update anything.'''
    (con, cur) = getConnection()
    
    cur.execute(
        '''select
            students.student_id,
            students.name,
            students.email,
            students.address,
            courses.course_name, 
            enrollments.enrollment_date
        from students
        join enrollments on enrollments.student_id = students.student_id
        join courses on courses.course_id = enrollments.course_id
        where students.student_id = ?
        ''', (sid, ))
    
    data = cur.fetchone()
    closeConnection(con, cur)
    
    if not data:
        return "NO such student exist."
    
    students = [{
        "student_id" : data[0],
        "name" : data[1],
        "email" : data[2],
        "address" : data[3],
        "course" : data[4],
        "enrollment_date" : data[5]
    }]
    
    return json.dumps(students, indent = 1)


@tool
def showAll():
    '''show all student information 
    if user asks show table or show all students information'''
    (con, cur) = getConnection()
    
    cur.execute(
        '''select
        students.student_id,
        students.name,
        students.email,
        students.address,
        courses.course_name,
        enrollments.enrollment_date
        from students
        join enrollments on enrollments.student_id = students.student_id
        join courses on courses.course_id = enrollments.course_id;
        ''')
    data = cur.fetchall()
    closeConnection(con, cur)
    
    students = []
    
    for student in data:
        students.append({
            "student_id" : student[0],
            "name" : student[1],
            "email" : student[2],
            "address" : student[3],
            "course" : student[4],
            "enrollment_date" : student[5],
        })
    
    return json.dumps(students, indent= 1)


@tool
def update(id, name, email, address, course):
    '''UPDATE an existing student's information.

    Use this tool when the user wants to:
    - update
    - change
    - modify
    - edit

    the student's name, email, address, or course.

    The student_id is required.

    DO NOT use showOne for update requests.'''
    
    (con, cur) = getConnection()
    
    cur.execute(
        '''select
            students.name,
            students.email,
            students.address,
            courses.course_name
        from students
        join enrollments 
            on enrollments.student_id = students.student_id
        join courses 
            on courses.course_id = enrollments.course_id
        where students.student_id = ?
        ''', (id, ))
    
    student = cur.fetchone()
    
    if not student:
        closeConnection(con, cur)
        return 'No such user exist.'
    # when not provided use previous one
    if not name:
        name = student[0]
    if not email:
        email = student[1]
    if not address:
        address = student[2]
    if not course:
        course = student[3]
        
    # update students table
    cur.execute(
        '''update students set
            name = ?,
            email = ?,
            address = ?
        where student_id = ?
        ''', (name, email, address, id))
    
    # update courses table
    cur.execute(
        '''update courses set
            course_name = ?
        where course_id = (
            select course_id from enrollments
            where student_id = ?
        )
        ''', (course, id))
    
    con.commit()
    changes = cur.rowcount
    closeConnection(con, cur)
    
    if changes >= 1:
        return 'Updated student successfully.'
    else:
        return 'Unable to update student.'


@tool
def delete(id):
    '''delete exisiting student details entirely having that id'''
    (con, cur) = getConnection()
    
    cur.execute("delete from enrollments where student_id =?",(id,))
    cur.execute("delete from students where student_id =?",(id,))
    
    con.commit()
    rows =cur.rowcount
    closeConnection(con, cur)
    if rows ==1:
        return 'Student deleted successfully'
    else:
        return 'Unable to delete student.'

'''have a great day!'''