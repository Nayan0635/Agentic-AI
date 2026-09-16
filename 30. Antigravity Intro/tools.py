#Here all Python driven functions has to be defined which AI will use as a tool.

#tool 1 : addition of 2 numbers
def addNumbers(a:int,b:int)->str:
    '''addition of 2 numbers'''
    return f"Sum={(a+b)}"


#tool 2: multipication of 2 numbers.
def multiNumbers(a:int,b:int)->str:
    '''multiplication of 2 numbers'''
    return f"Multiplication={(a*b)}"


#tool 3: saving content to local file i.e hello.txt
def saveFile(content:str)->str:
    '''saving content to local file i.e hello.txt'''
    with open("./hello.txt","w+") as file:
        file.write(content)
        file.close()
        return 'File created successfully'

#tool 4: reading from the created file
def readFile()->str:
    """
    Read the contents of the previously created hello.txt file.

    This tool does not require any arguments.
    Do not provide any parameters when calling this tool.
    """
    with open("./hello.txt","r+") as file:
        data =file.read()
        file.close()
        return data
    