'''
List[]:
    list in python is a data container or data structure that can hold
    objects of different data types.
    
'''

if __name__ == "__main__":
    '''store different data types'''
    lst = ['nayan', True, 2026, 100.235] # containing different data type
            # 0      1     2     3     forward indexing
            #-4     -3     -2    -1    backward indexing
    '''elements always maintain insertion ordering'''
    print(lst)
    '''(i) follows indexing means can accesss elements using indices'''
    print(lst[2])
    print(lst[-2])
    
    '''(ii) it allows replication can hold duplicate values'''
    lst = lst*2
    print(lst)
    
    '''(iii) list is mutable means we can edit after creating a list'''
    lst.insert(3, "Kolkata") # insert at index 3
    print(lst)
    
    
    lt = []
    lt.append(2)
    print(lt)
    lt.remove(2)
    print(lt)