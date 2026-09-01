st = input("Enter a string: ")

temp = st
# for c in st:
#     temp.append(c)  #append
    
flag = True
for i in range(0, len(temp)):
    if temp[i].upper() != temp[len(temp)-i-1].upper():
        flag = False
        break
if flag:
    print(f"{st} is Palindrome")
else:
    print(f"{st} is Not Palindrome")