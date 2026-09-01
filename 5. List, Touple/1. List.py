lst = [21, 'CN', True, 3.14,]

#      -4   -3    -2    -1    backward indexing

print(lst[0]) #forward indexing
print(lst[-4]) #backward indexing

lst[0] = 1000 #rewrite the value
print(lst)


lst.insert(3, "Kolkata") #insert at index 3 shift other element
print(lst)
print()

for item in lst:
    print(item, end = "\n")
print()    
    
lst.reverse()
print(lst)

# Reverse Manually

# did someting
# traverse from back
for i in range(len(lst) -1, -1, -1):
    print(lst[i])
    
# backward index
for i in range(-len(lst), 0, 1):
    print(lst[i])
    
print("Reversing: ")
left = 0
right = len(lst) - 1

while(left < right):
    lst[left], lst[right] = lst[right], lst[left]
    left+= 1
    right-= 1

# Replication
lst *= 3
print(lst)

num1 = [1, 2, 3] #explain
num3 = num1.copy()  #deep copy --> creates another copy
# num2 = num1        #Sallow copy -->pointing to same memory location

# num2.remove(2)
num3.remove(2)

print(num1, num3, sep = '\n')
    