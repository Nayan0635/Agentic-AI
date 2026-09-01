from connection import getConnection
import json

def addStudents(student_name, student_email, course_name):
    (con, cursor) = getConnection()
    cursor.execute("insert into students(name,email) values(?,?)",(student_name, student_email))
    student_id = cursor.lastrowid
    # --->course
    cursor.execute("select course_id from courses where course_name=?",(course_name,))
    course = cursor.fetchone() #get matching course

    if course: #if already there
        course_id = course[0]
    else: #if not there add new
        cursor.execute("insert into courses(course_name) values(?)",(course_name,))
        course_id = cursor.lastrowid
    # ---->enrollment
    cursor.execute("insert into enrollments(student_id,course_id) values(?,?)",(student_id, course_id))
    con.commit()

    rows = cursor.rowcount #last updated no of rows..

    cursor.close()
    con.close()
    if rows == 1:
        return "One Student Successfully Added"
    else:
        return "Unable to Add Student"

def updateStudents(sid, sname, semail, course):
    # Updating student details along with course..
    (con, cursor) = getConnection()
    cursor.execute("select name,email from students where student_id=?",(sid,))
    student = cursor.fetchone()

    if not student:
        cursor.close()
        con.close()
        return "Student Not Found" #go out
    if not sname:
        sname = student[0]
    if not semail:
        semail = student[1]

    cursor.execute('''
    update students
    set name=?,
        email=?
    where student_id=?
    ''', (sname, semail, sid))

    if course:
        cursor.execute("select course_id from courses where course_name=?",(course,))
        c = cursor.fetchone()
        if c:
            course_id = c[0]
        else:
            cursor.execute("insert into courses(course_name) values(?)",(course,))
            course_id = cursor.lastrowid
        cursor.execute("update enrollments set course_id=? where student_id=?",(course_id, sid))
    
    con.commit()
    rows = cursor.rowcount
    cursor.close()
    con.close()
    if rows == 1:
        return "Student Profile successfully Updated"
    else:
        return "Unable to Update student"

def deleteStudent(sid):
    # Delete student along with enrollment
    (con, cursor) = getConnection()
    # foreign key support PRAGMA
    cursor.execute("delete from students where student_id=?",(sid,))

    con.commit()
    rows = cursor.rowcount
    cursor.close()
    con.close()
    if rows == 1:
        return "One Student Deleted Successfully"
    else:
        return "Unable to Delete Student"

def showStudents():

    (con, cursor) = getConnection()

    cursor.execute('''
    SELECT students.name,
           students.email,
           courses.course_name,
           enrollments.enroll_date
    FROM enrollments
    INNER JOIN students
    ON enrollments.student_id = students.student_id
    INNER JOIN courses
    ON enrollments.course_id = courses.course_id
    ''')

    students = cursor.fetchall()
    cursor.close()
    con.close()

    data = []
    for student in students:
        data.append({
            "student_name": student[0],
            "email": student[1],
            "course": student[2],
            "enroll_date": student[3]
        })
    return json.dumps(data, indent=1) # for formatting
    # return students

def countStudents():
    (con, cursor) = getConnection()
    cursor.execute('''
    SELECT courses.course_name,
           COUNT(enrollments.student_id)
    FROM courses
    INNER JOIN enrollments
    ON courses.course_id = enrollments.course_id
    GROUP BY courses.course_name
    ''')

    students = cursor.fetchall()
    cursor.close()
    con.close()
    data = []
    for student in students:
        data.append({
            "course": student[0],
            "no of students": student[1]
        })
    return json.dumps(data, indent=1)
    # return students
