from connection import *
import json

def addNew(name, email, address, course):
    (con, cursor) = getConnection()

    try:
        # Add student if email does not already exist
        cursor.execute(
            '''INSERT OR IGNORE INTO students(name, email, address)
            VALUES (?,?,?)''',(name, email, address))
        # Get student_id
        cursor.execute("SELECT student_id FROM students WHERE email = ?",(email,))
        student = cursor.fetchone()
        if not student:
            return "Unable to add student."
        student_id = student[0]

        cursor.execute('''INSERT OR IGNORE INTO courses(course_name)VALUES (?)''',(course,))
        # Get course_id
        cursor.execute(
            "SELECT course_id FROM courses WHERE course_name = ?",
            (course,)
        )
        course_data = cursor.fetchone()
        if not course_data:
            return "Unable to add course."
        course_id = course_data[0]

        # use ids to add in enrollments
        cursor.execute(
            '''
            INSERT OR IGNORE INTO enrollments(student_id, course_id)
            VALUES (?, ?)
            ''',(student_id, course_id)
        )

        con.commit()

        return "Student added successfully."

    except Exception as e:
        con.rollback()
        return f"Unable to add student: {e}"
    finally:
        closeConnection(con, cursor)


def showALL():
    (con, cursor) = getConnection()

    cursor.execute(
        '''SELECT
            students.student_id,
            students.name,
            students.email,
            students.address,
            courses.course_name,
            enrollments.enrollment_date
        FROM students
        JOIN enrollments ON students.student_id = enrollments.student_id
        JOIN courses ON courses.course_id = enrollments.course_id;''')
    data = cursor.fetchall()

    students = []

    for student in data:
        students.append({
            "student_id": student[0],
            "name": student[1],
            "email": student[2],
            "address": student[3],
            "course": student[4],
            "enrollment_date": student[5]
        })

    closeConnection(con, cursor)

    return json.dumps(students, indent=1)