x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x > y:
    print("x is greater than y")
    print(f"greater = {x} \n smaller = {y} ")
else:
    print("y is greater than x")


avg = (x + y) / 2
print("Average = ", avg)