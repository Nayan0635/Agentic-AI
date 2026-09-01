x = int(input("Enter 1 for INR to USD and 2 for USD to INR: "))
curr = int(input("Enter currency: "))

if x == 1:
    print(f"{curr} INR is {curr/94.95:.2f} USD")
    
elif x == 2:
    print(f"{curr} USD is {curr*94.95:.2f} INR")
    

# c/5 = (f-32)/9  
# x = int(input("Enter 1 for C to F and 2 for F to C : "))
# temp = int(input("Enter temp: "))

# if x == 1:
#     f = (temp * 9/5) + 32
#     print(f"{curr} in c is {f:.2f} F")
    
# elif x == 2:
#     c = (temp - 32) * 5/9
#     print(f"{temp} f is {c:.2f} C")