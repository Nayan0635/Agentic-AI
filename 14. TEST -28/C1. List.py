lst = []

# take user input
for it in range(0, 5, 1):
    n = int(input("entre: "))
    lst.append(n)
print(lst)


# find maxi, mini, avg
maxi = lst[0]
mini = lst[0]
cnt = 0
total = 0

for it in lst:
    if it > maxi:
        maxi = it
    if it < mini:
        mini = it
    cnt+= 1
    total += it

avg = total/cnt

print("Maximum: ", maxi)
print("Minimum: ", mini)
print("Average: ", avg)