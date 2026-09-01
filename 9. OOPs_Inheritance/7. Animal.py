## Question 2: Animal → Dog → Puppy

# Create a Java program using multilevel inheritance.

# * Class `Animal`

#   * Method: `eat()`

# * Class `Dog` extends `Animal`

#   * Method: `bark()`

# * Class `Puppy` extends `Dog`

#   * Method: `play()`

# Create an object of `Puppy` and call all three methods.

# **Expected Output**

# ```
# Animal is eating
# Dog is barking
# Puppy is playing
# ```




class Animal:
    def eat(self):
        print(f"Animal is eating")
        
class Dog(Animal):
    def bark(self):
        self.eat()
        print(f"Dog is barking")
        
        
        
class Puppy(Dog):
    def play(self):
        self.bark()
        print(f"Puppy is playing")
        
        
# Main()
ani = Puppy()
ani.play()