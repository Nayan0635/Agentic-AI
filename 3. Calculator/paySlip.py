name = input("Enter Employee Name: ")
basic = int(input("Enter Basic Salary: "))

DA, HRA, TDS = 0.02, 0.03, 0.01

DA *= basic
HRA *= basic
TDS *= basic

GPay = basic + DA + HRA - TDS


print("Generating Pay Slip",end = "\n====================\n")

print(f"Employee Name: {name}")
print(f"Basic Salary: {basic}")
print(f"DA: {DA}")
print(f"HRA: {HRA}")
print(f"TDS: {TDS}")
print(f"Gross Pay: {GPay}")