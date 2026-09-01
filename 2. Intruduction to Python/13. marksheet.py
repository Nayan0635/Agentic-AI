print("Enter paper numbers..")
e = int(input("english: "))
m = int(input("math: "))
s = int(input("science: "))

avg = (e + m + s)/3
total = (e + m + s)
print(f"Average ={avg: .2f}, Total = {total}")


if avg>= 80 and avg <= 100:
    print("Grade : A")
elif avg>= 60 and avg <= 79:
    print("Grade : B")
elif avg>= 40 and avg <= 59:
    print("Grade : C")
else:
    print("Fail")