# num = int(input("Enter the number: "))
num = 3214

# 3.214
thousand = num//1000
print(thousand)

# 32.14 remainder 2
hundred = (num//100)%10
# remainder = 214 then 2.14
_hundread = (num%1000)//100
print(_hundread)

# 321.4 remainder 1
tens = (num//10)%10
print(tens)

ones = num%10
print(ones)