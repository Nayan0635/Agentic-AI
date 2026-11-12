def addNumbers(a:int,b:int)->str:
    '''addition of 2 numbers'''
    return f"Sum={(a+b)}"


def multiNumbers(a:int,b:int)->str:
    '''multiplication of 2 numbers'''
    return f"Multiplication={(a*b)}"


def saveFile(content:str)->str:
    '''saving content to local file i.e hello.txt'''
    with open("./hello.txt","w+") as file:
        file.write(content)
        file.close()
        return 'File created successfully'

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
    