
s = int(input("How many employee? "))

employee = {}
for e in range(0, s, 1):
    employee[e] = {}
    
    employee[e]["empid"] = int(input("Enter employee id: "))
    employee[e]["name"] = input("Enter employee name: ")
    employee[e]["salary"] = int(input("Enter employee salary: "))
    
for e in employee:
    print(f"empid : {employee[e]["empid"]}")
    print(f"name : {employee[e]["name"]}")
    print(f"salary : {employee[e]["salary"]}")