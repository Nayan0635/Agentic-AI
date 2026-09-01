from connection import getConnection
import json


def addStudents(student_name:str,student_email:str,course_name:str,course_fees:float)->str:
    '''
       Adding a new student along with course details into the both of the targeted table
       i.e students another one is courses.
    '''
    (con,cursor) = getConnection()
    cursor.execute("insert into students(name,email)values(?,?)",(student_name,student_email))
    #we will get last row id 
    student_id=cursor.lastrowid
    cursor.execute("insert into courses(course_name,course_fees,student_id)values(?,?,?)",(course_name,course_fees,student_id))
    con.commit()
    rows = cursor.rowcount
    #Database connection.
    cursor.close()
    con.close()
    if rows ==1:
        return 'One Student successfully Added'
    else:
        return 'Unable to Add a new Student'


def getStudents():
    (con,cursor)= getConnection()
    cursor.execute('''
       select students.name,
       students.email,
       courses.course_name
       from students inner JOIN courses
       on(students.student_id = courses.course_id);
       
''')
    students = cursor.fetchall()
    cursor.close()
    con.close()
    data = [] #empty list
    for student in students:
        data.append({
            "student_name":student[0],
            "email":student[1],
            "course":student[2]
        })
    return json.dumps(data,indent=1)

def countStudents():
    (con,cursor) = getConnection()
    cursor.execute('''
    select count(students.name) as 'no of students',
       courses.course_name
       from students inner join courses
       on(students.student_id = courses.student_id)
       group by courses.course_name;
       
''')
    students = cursor.fetchall()
    data = []
    for student in students:
        data.append({
            'course':student[1],
            'no of students ':student[0]
        })
    cursor.close()
    con.close()
    return json.dumps(data,indent=1)    

#Show those students who are doing more than equal 2 courses at the same time.
#Sort by no of students doing courses.
#course_name should be input and students doing the course will be output.

def updateStudents(sid:int,sname:str,semail:str,course:str,fees:str)->str:
  '''updating courses and students table simultaneously'''
  (con,cursor) = getConnection()
  cursor.execute('''
   select students.name,
       students.email,
       courses.course_name,
       courses.course_fees
       from students inner JOIN courses
       on(students.student_id = courses.course_id)
                 and students.student_id=?
                 
''',(sid,))
  student=cursor.fetchone()
  if not sname :
      sname = student[0]
  if not semail:
      semail = student[1]
  if not course:
      course = student[2]
  if not fees:
      fees = student[3]
  cursor.execute('''
   update students set name=?,
                       email=?
                       where student_id=?
''',(sname,semail,sid))
  cursor.execute('''
   update courses set course_name=?,
                      course_fees=?
                      where student_id=?  
''',(course,fees,sid))
  con.commit()
  rows =cursor.rowcount
  cursor.close()
  con.close()
  if rows == 1:
      return 'Student Profile successfully Updated'
  else:
      return 'Unable to Update Students Profile'

def deleteStudent(sid:int)->str:
    '''deleting student as database is on cascade delete it will delete course also'''
    (con,cursor)= getConnection()
    # Enable Foreign Key Support
    con.execute("PRAGMA foreign_keys = ON")
    cursor.execute("delete from students where student_id=?",(sid,))
    con.commit()
    rows =cursor.rowcount
    cursor.close()
    con.close()
    if rows ==1:
        return 'One student deleted successfully'
    else:
        return 'Unable to delete. '