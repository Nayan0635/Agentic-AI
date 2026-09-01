a, b, c = map(int, input("Enter numbers: ").split())

# greater = max(a, b, c)

greater = a if a > b and a > c else (b if b > c else c)
print(greater)