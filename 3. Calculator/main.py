print("Welcome to calculator app!", end = "\n==========================\n")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Integer Dvision")
print("5. Maximum Number")
print("5. Minimum Number")
print("5. Average")
print("6. Exit\n")


x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))


# Calling user define modules
from function import *

while True:
    choice = int(input("\nEnter your choice (1-9): "))
    
    if choice == 1:
        # print(f"Addition = : {x + y}")
        sum = add(x, y)
        print(f"Addition = : {sum}")
        
    elif choice == 2:
        # print(f"Subtraction = : {x - y}")
        sub = sub(x,y)
        print(f"Subtraction = : {sub}")
        
    elif choice == 3:
        # print(f"Multiplication = : {x * y}")
        mul = mul(x,y)
        print(f"Multiplication = : {mul}")
        
    elif choice == 4:
        # print(f"Division = : {(x/y):.2f}")
        div = div(x,y)
        print(f"Division = : {div:.2f}")
        
    elif choice == 5:
        # print(f"Integer Division = : {x//y}")
        int_div = int_div(x,y)
        print(f"Integer Division = : {int_div}")
        



    elif choice == 6:
        # print(f"Maximum No = : {max(x,y)}")
        maxi = maxi(x,y)
        print(f"Maximum No = : {maxi}")
        
    elif choice == 7:
        # print(f"Minimum No = : {min(x,y)}")
        mini = mini(x,y)
        print(f"Minimum No = : {mini}")
        
    elif choice == 8:
        # print(f"Average No = : {(x+y)/2}")
        ave = ave(x,y)
        print(f"Average No = : {ave}")
        
    elif choice == 9:
        print("Exit")
        exit(0)