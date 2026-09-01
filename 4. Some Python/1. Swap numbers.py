a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print(f"Before swapping: a = {a}, b = {b}")

# using third variable
# c = a
# a = b
# b = c


# without using third variable
b = a + b - (a:= b) 

# a,b = b,a

print(f"After swapping: a = {a}, b = {b}")