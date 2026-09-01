# n = int(input("Enter Number: "))
n = 4 

for i in range(n+1):
    for j in range(1, i + 1):
        print(f"*", end = "")
    print()
print()


for i in range(n):
    for j in range(n, i, -1):
        print(f"*", end = "")
    print()
print()
 
for i in range(n):
    for j in range(n, i, -1):
        print(f"B", end = "")
    for k in range(0, i + 1):
        print(f"*", end = "")
    print()
print()


for i in range(n):
    for k in range(0, i + 1):
        print(f"B", end = "")
    for j in range(n, i, -1):
        print(f"*", end = "")
    print()
print()


for i in range(n):
    for k in range(n, i, -1):
        print(f"B", end = "")
    for j in range(0, (2*i) + 1):
        print(f"*", end = "")
    print()
print()


# i-> 0 1 2 3 4
# j-> 0 1 2 3 4
# k-> 9 7 5 3 1  (2*n -i)

for i in range(n):
    for j in range(0, i + 1):
        print(f"B", end = "")
        
    for k in range(2*n -1, 2*i, -1):
    # for k in range(2*n -2*i -1):
        print(f"*", end = "")
    print()



