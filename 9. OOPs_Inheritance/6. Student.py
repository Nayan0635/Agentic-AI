## Question 1: Student → Exam → Result


# * Create a class `Student`

#   * Data member: `name`
#   * Method: `getStudent()`

# * Create a class `Exam` that inherits `Student`

#   * Data member: `marks`
#   * Method: `getMarks()`

# * Create a class `Result` that inherits `Exam`

#   * Method: `displayResult()`

# **Output Example**

# ```
# Student Name: Rahul
# Marks: 85


class Student:
    def __init__(self, name):
        self.name = name
        
    def getStudent(self):
        print(f"Student Name : {self.name}")
        
class Exam(Student):
    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks
        
    def getMarks(self):
        super().getStudent()
        print(f"Marks : {self.marks}")
        
class Result(Exam):
    def __init__(self, name, marks):
        super().__init__(name, marks)
        
    def displayResult(self):
        super().getMarks()
        
        
# Main()
stu = Result('Rahul', 99)
stu.displayResult()