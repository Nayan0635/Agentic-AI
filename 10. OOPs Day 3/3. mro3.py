## Question 3 (Medium)

# Create the following hierarchy:

# ```text
#         A
#       /   \
#      B     C
#       \   /
#         D
# ```

# Each class has a method `show()`.

# Use `super()` correctly so every class method executes only once.

# Print the MRO of class `D`.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

class C(A):
    def show(self):
        super().show()
        print("Class C")

class D(B, C):
    def show(self):
        super().show()
        print("Class D")

ob = D()
ob.show()
print(D.mro())
