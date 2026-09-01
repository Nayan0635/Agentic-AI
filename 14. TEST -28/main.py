from crud import *

while True:
    print('''
    1. Add new Student
    2. Update Student details
    3. Delete Student data using id
    4. Show Students by their courses and enrollment
    5. Count Students Per Course
    6. Exit
    ''')
    choice = int(input("Enter Your Choice (1-6): "))
    
    if choice == 1:
        sname = input("Student Name : ")
        semail = input("Student Email : ")
        scourse = input("Course Name : ").upper()
        print(addStudents(student_name=sname,student_email=semail,course_name=scourse))
    
    elif choice == 2:
        sid = int(input("Student ID : "))
        sname = input("New Name (press enter to skip) : ")
        semail = input("New Email (press enter to skip) : ")
        course = input("New Course (press enter to skip) : ").upper()
        print(updateStudents(sid=sid,sname=sname,semail=semail,course=course))

    elif choice == 3:
        sid = int(input("Student ID : "))
        deleteChoice = input("Do You Want To Delete? (Y/N): ")
        if deleteChoice == 'Y' or deleteChoice == 'y':
            print(deleteStudent(sid))
        # else --> what if N do this --> go back to menu?

    elif choice == 4:
        print(showStudents())

    elif choice == 5:
        print(countStudents())    
    
    elif choice == 6:
        print("Thank you see ya")
        exit(0)