# Question 1: Single Inheritance (Basic)

# Create a class `Person` with:

# * Constructor accepting `name`
# * Method `display()`

# Create a class `Student` that inherits from `Person`.

# Requirements:

# * Constructor accepts `name` and `roll`
# * Use `super()` to call the parent constructor.
# * Override the `display()` method.
# * Use `super().display()` inside the child class.

# Expected Output

# Name : Rahul
# Roll : 101

class Person:
    def __init__(self, name):
        self.name = name
        
    def display(self):
        print(f"Name : {self.name}")

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
        super().display()
        print(f"Roll : {self.roll}")
        
name = input("Enter name: ")
roll = input("Enter roll: ")

stu = Student(name, roll)
stu.display()

