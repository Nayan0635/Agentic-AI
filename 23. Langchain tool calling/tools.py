from langchain_core.tools import tool

@tool
def addNumbers(a:int,b:int)->str:
    '''addition of 2 numbers'''
    return f'Sum of 2 Number is ={(a+b)}'

@tool
def multiplyNumbers(a:int,b:int)->str:
    '''multipication of 2 numbers'''
    return f'Multiply Result={(a*b)}'

@tool
def saveFile(content:str)->str:
    '''saving content to local file i.e hello.txt'''
    with open("./hello.txt","w+") as file:
        file.write(content)
        file.close()
        return 'File created successfully'

@tool
def readFile()->str:
    '''reading from created file i.e hello.txt'''
    with open("./hello.txt","r+") as file:
        data = file.read()
        file.close()
        return data

'''gemini doesn't understand until you write like this -> (sci: int, math: int, eng: int) -> str'''

@tool
def total(sci: int, math: int, eng: int) -> str:
    '''Calculating only total marks of 3 Subjects'''
    return f'Total marks of student is = {(sci+math+eng)}'

@tool
def avg(sci: int, math: int, eng: int) -> str:
    '''Calculating only average of 3 subjects'''
    return f'Student average mark is = {(sci+math+eng)/3}'

@tool
def gradation(sci: int, math: int, eng: int) -> str:
    '''Calculate only student grade based on marks of 3 subjecs'''
    total = sci+ math+ eng
    avg = total/3
    
    if avg >= 80 and avg <= 100:
        return f'Student grade is A.'
    elif avg >= 60 and avg <= 79:
        return f'Student grade is B.'
    elif avg >= 41 and avg <= 59:
        return f'Student grade is C.'
    else:
        return f'Student FAILD.'
    
    
@tool
def score(sci: int, math: int, eng: int) -> str:
    '''
    Use this tool ONLY when the user asks for the complete student score/result,
    including ALL THREE:
    1. total marks
    2. average marks
    3. grade

    Do NOT use this tool when the user asks only for total, only for average,
    or only for grade.
    '''
    
    total_marks = total.invoke({"sci": sci, "math": math, "eng": eng})
    average_number = avg.invoke({"sci": sci, "math": math, "eng": eng})
    grade = gradation.invoke({"sci": sci, "math": math, "eng": eng})
    return f'\n{total_marks}, \n{average_number}, \n{grade}'