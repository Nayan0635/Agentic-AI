# Question 2: Single Inheritance (Employee)

# Create a class `Employee`.

# Data Members:

# * name
# * salary

# Methods:

# * Constructor
# * `show()`

# Create a class `Manager` inheriting from `Employee`.

# Requirements:

# * Add one more attribute `department`
# * Use `super()` to initialize inherited attributes.
# * Call `super().show()` before displaying the department.

# Expected Output

# Employee Name : Amit
# Salary : 50000
# Department : HR




class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show(self):
        print(f"Name : {self.name}")
        print(f"Salary : {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def show(self):
        super().show() 
        print(f"Department : {self.department}")
        
# Main()
name = input("Enter name: ")
salary = input("Enter salary: ")
Department = input("Enter Department: ")

emp = Manager(name, salary, Department)
emp.show()