## Question 3: Employee → Manager → Director

# Create a Java program using multilevel inheritance.

# * Class `Employee`

#   * Variables: `empId`, `name`

# * Class `Manager` extends `Employee`

#   * Variable: `department`

# * Class `Director` extends `Manager`

#   * Variable: `salary`
#   * Method: `display()`

# Display all employee details.

# **Sample Output**

# ```
# Employee ID : 101
# Name        : Amit
# Department  : IT
# Salary      : 95000


class Employee:
    def __init__(self, empID,  name):
        self.empID = empID
        self.name = name
        
    def getEmployee(self):
        print(f"Employee ID : {self.empID}")
        print(f"Employee Name : {self.name}")
        
class Manager(Employee):
    def __init__(self, empID, name, department):
        super().__init__(empID, name)
        self.department = department
        
    def getDepartment(self):
        super().getEmployee()
        print(f"Department : {self.department}")
        
class Director(Manager):
    def __init__(self, empID, name, department, salary):
        super().__init__(empID, name, department)
        self.salary = salary
        
    def display(self):
        super().getDepartment()
        print(f"Salary : {self.salary}")
        
        
# Main()
emp = Director(101, 'Rahul','IT', 95000)
emp.display()