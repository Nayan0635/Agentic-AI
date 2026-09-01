num = int(input("Enter a number: "))
sum = 0

# for i in range(1, num + 1, 1):
#     sum = i**3 - i**2
#     print(f"{sum}", end=" ")


a,b = 0, 1
print(f"{a} {b}", end=" ")
for i in range(1, num + 1, 1):
    a, b = b, a + b
    print(f"{b}", end=" ")