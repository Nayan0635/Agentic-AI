def addNumbers(a:int,b:int)->int:
    '''adding 2 numbers'''
    return a+b

def multiplyNumbers(a:int,b:int)->int:
    '''multiply or product of 2 numbers'''
    return a*b


#----------------Save & Read file ----------------------#
def saveFile(content:str)->str:
    '''saving content to local file i.e hello.txt'''
    with open("./hello.txt","w+") as file:
        file.write(content)
        file.close()
        return 'File created Successfully'
def readFile()->str:
    '''reading content from the file created before i.e hello.txt'''
    with open("./hello.txt","r+") as file:
        data = file.read()
        file.close()
        return data