## Question 5: Person → Teacher → Principal

# * Class `Person`

#   * Variable: `name`

# * Class `Teacher` extends `Person`

#   * Variable: `subject`

# * Class `Principal` extends `Teacher`

#   * Variable: `schoolName`
#   * Method: `displayDetails()`

# Display all details.

# **Sample Output**

# ```
# Name       : Suman
# Subject    : Mathematics
# School     : ABC Public School

class Person:
    def __init__(self, name):
        self.name = name
        
    def getPerson(self):
        print(f"name : {self.name}")
        
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
    def getsubject(self):
        super().getPerson()
        print(f"subject : {self.subject}")
        
class Principal(Teacher):
    def __init__(self, name, subject, schoolName):
        super().__init__(name, subject)
        self.schoolName = schoolName
        
    def display(self):
        super().getsubject()
        print(f"School : {self.schoolName}")
        
# Main()
stu = Principal('Suman', 'Mathermatics', 'ABC Public School')
stu.display()