def addNumbers(a:int,b:int)->int:
    '''adding of 2 numbers'''
    return a+b

def saveFile(content:str)->str:
    '''saving content to local file i.e hello.txt'''
    with open("./hello.txt","w+") as file:
        file.write(content)
        file.close()
        return 'file created successfully'

def readFile()->str:
    '''reading content from created file i.e hello.txt'''
    with open("./hello.txt","r+")as file:
        data = file.read()
        file.close()
        return data