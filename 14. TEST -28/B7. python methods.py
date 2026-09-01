lst = [13, 62, 34, 49, 26] #created a empty list

'''append()'''
lst.append(5) #inserting at the end 
print(lst)

'''remove()'''
lst.remove(5) #delete element
print(lst)
lst.remove(lst[len(lst) -1]) #delete using index
print(lst)

'''sort()'''
lst.sort()
print(lst)
