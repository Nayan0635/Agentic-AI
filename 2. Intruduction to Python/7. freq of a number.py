num = int(input("Enter number: "))

s = str(num)

second_digit = s[1]

for ch in s:
    if ch == second_digit:
        flag += 1

print(f"{second_digit} is repeated {flag} times in {s}")