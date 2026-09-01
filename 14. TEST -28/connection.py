# 4.Create a Database named as studentsDB which will have following
# tables students(student_id integer primary key autoincrement,
# name text ,
# email text unique
# )
# course table : course_id , course_name
# enrollments : enroll_id,enroll_date default CurrentDate,student_id,course_id




# Perform crud operations
# 1)user will enter student name.course name and data will be distributed among three
# tables.
# 2)Update student details along with course
# 3)Delete student along with course
# 4)Show all student by their courses and enrollments
# 5)count students per courses


import sqlite3
import os

def getConnection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database", "studentsDB.sqlite3")

    con = sqlite3.connect(db_path)
    con.execute("PRAGMA foreign_keys = ON")
    cursor = con.cursor()
    
    return con, cursor