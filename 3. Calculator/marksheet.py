name = input("Enter student name: ")
e = int(input("mark of english: "))
s = int(input("mark of science: "))
m = int(input("mark of math: "))

avg = (e + m + s)/3
total = (e + m + s)

Grade = ""
if avg>= 80 and avg <= 100:
    Grade = "A"
    print("Grade : A")
elif avg>= 60 and avg <= 79:
    Grade = "B"
    print("Grade : B")
elif avg>= 40 and avg <= 59:
    Grade = "C"
    print("Grade : C")
else:
    Grade = "Fail"
    print("Fail")



print(f"Student Name: {name}")
print(f"mark of english: {e}")
print(f"mark of science: {s}")
print(f"mark of math: {m}")
print(f"Average ={avg: .2f}, Total = {total}")
print(f"Grade : {Grade}")
