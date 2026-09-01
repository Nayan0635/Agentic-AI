from functions import MyClass
# import os
# print(os.getcwd())#use it to know current working directory


if __name__ == "__main__":
    while True:
        emp = MyClass()
        print('''
    1. View all employees
    2. Get employee detail enter id
    3. Register new Employee
    4. Update an Employee details
    5. Delete an Employee
    6. Exit
        ''')
        
        choice = int(input("Your choice ? "))
        
        if choice == 1:
            emp_names = emp.getEmployees()
            for e in emp_names:
                print(e[0], e[1], e[2], e[3])
        
        elif choice == 2:
            id = int(input("Enter that employee id: "))
            e = emp.findEmployee(id)
            if not e:
                print("cann't find anyone ☹️")
            else:
                print(e[1], e[2], e[3])
        
        elif choice == 3:
            _name = input("Enter name: ")
            _mail = input("Enter mail: ")
            _salry = int(input("Enter salary: "))
            print(emp.addEmployee(_name, _mail, _salry))
        
        elif choice == 4:
            id = int(input("Enter id: "))
            _name = input("Enter name: ")
            _mail = input("Enter mail: ")
            _salry = int(input("Enter salry: "))
            print(emp.updateEmp(id, _name, _mail, _salry))
        
        elif choice == 5:
            id = int(input("Gimme id: "))
            print(emp.deleteEmployee(id))

        elif choice == 6:
            #XXX Database Connection has to be closed .    
            emp.cursor.close()
            emp.con.close()
            print("see ya ☺️")
            exit(0)
        # elif choice == 2:
        # elif choice == 2: