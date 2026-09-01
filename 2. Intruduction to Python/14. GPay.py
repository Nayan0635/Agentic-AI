b = int(input())

DA, HRA, TDS = 0.02, 0.03, 0.01

DA *= b
HRA *= b
TDS *= b

GPay = b + DA + HRA - TDS
print(f"Gross Pay {GPay}: ")