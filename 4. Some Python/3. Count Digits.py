n = int(input("Enter number: "))

temp = n
cnt = 0
digits = 0

reverse = 0
armstrong = 0

while temp > 0:
    digits = temp % 10
    print(f"{digits} ", end="")
    
    reverse = reverse * 10 + digits
    armstrong += digits ** 3
    
    temp = temp // 10
    cnt += 1
    
print(f"\n{n} is {cnt} digits long.")


if n == reverse:
    print(f"{n} is an Palindrome number.")
else:
    print(f"{n} is not an Palindrome number.")
    

if n == armstrong:
    print(f"{n} is an armstrong number.")
else:
    print(f"{n} is not an armstrong number.")
    