# Create three classes:


# A
# |
# B
# |
# C
# ```

# Each class has a method `display()`.

# Inside `display()`, use `super()` to call the parent method.

# Expected Output:

# ```
# Class A
# Class B
# Class C
# ```

# Also print the MRO.

class A:
    def display(self):
        print("Class A")
class B(A):
    def display(self):
        super().display()
        print("Class B")
class C(B):
    def display(self):
        super().display()
        print("Class C")

ob = C()
ob.display()
print(C.mro())