num = int(input("Enter a number to calculate factorial: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
    print(f"{fact}")
print(f"Factorial of {i} is {fact}")