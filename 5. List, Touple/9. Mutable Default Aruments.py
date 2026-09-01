# def addItems(items = []):  #default aruments are evaluated once, wen defined not when it's called
#     items.append('New')
#     print(items)


def addItems(items = None):
    if items is None: #if no list passed
        items = []    #create a new list every time
        items.append('New')
        print(items)
    
    
addItems()
addItems()
addItems()