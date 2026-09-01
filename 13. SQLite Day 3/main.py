from crud import *
if __name__=="__main__":
    print("1.Add a new Student:")
    print("2.get Students by Their courses :")
    print("3.Count students under courses:")
    print("4.Update Student Records :")
    print("5.Delete Student Info:")
    print("6.Exit")
while True:
    choice = int(input("Enter Your choice between 1-6:"))
    if choice == 1:
        sname = input("Student Name:")
        semail= input("Student email:")
        scourse= input("Course Name:").upper()
        sfees  = float(input("Course Fees:"))
        print(addStudents(student_name=sname,student_email=semail,course_name=scourse,course_fees=sfees))
    elif choice == 2:
        print(getStudents())
    elif choice == 3:
        print(countStudents())
    elif choice == 4:
        sid  = int(input("Enter Student id :"))
        sname = input("New student Name or press enter to skip")
        semail= input("New Email or press enter to skip")
        course= input("New Course or Hit enter to skip")
        fees  = float(input("Fees or Hit enter to skip:"))
        print(updateStudents(sid=sid,sname=sname,semail=semail,course=course,fees=fees))
    elif choice == 5:
        sid = int(input("Enter Student id:"))
        deleteChoice = input("Do You want  to Delete This Record? Y/N ")
        if deleteChoice =='Y' or deleteChoice =='y':
            print(deleteStudent(sid))
    elif choice == 6:
        print("Thank You Bye Bye")
        exit(0)

