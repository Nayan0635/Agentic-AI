lst = [34, 56, 12, 67, 27, 44]

# maxi = max(lst)
# print("Maximum Number: ", maxi)

# mini = min(lst)
# print("Minimum Number: ", mini)

# avg = sum(lst)/ len(lst)
# print(avg)

maxi = lst[0]
mini = lst[0]
cnt = 0
sum = 0

for it in lst:
    if it > maxi:
        maxi = it
    if it < mini:
        mini = it
    cnt+= 1
    sum += it

avg = sum/cnt

print("Maximum: ", maxi)
print("Minimum: ", mini)
print("Average: ", avg)