# Question 3: Multilevel Inheritance (School)
# Create three classes.
# Person
#    ↑
# Student
#    ↑
# Result
# ```

# Requirements

# Person
# * name
# Student
# * roll number
# Result
# marks

# Use `super()` in every constructor.

# Create a method that displays()
# Name
# Roll
# Marks


class Person:
    def __init__(self, name):
        self.name = name
        
class Student(Person):
    def __init__(self, name, rollNumber):
        super().__init__(name)
        self.rollNumber = rollNumber
        
class Result(Student):
    def __init__(self, name, rollNumber, marks):
        super().__init__(name, rollNumber)
        self.marks = marks
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll : {self.rollNumber}")
        print(f"Marks : {self.marks}")
        
        
# Main()
stu = Result('student', 132, 95)
stu.display()