# defining all functionalities of the project here.

def add(a:int, b:int) -> int:
    return a + b
def sub(a:int, b:int) -> int:
    return a - b
def mul(a:int, b:int) -> int:
    return a * b
def div(a:float, b:float) -> float:
    return a / b
def int_div(a:int, b:int) -> int:
    return a // b


def maxi(a:int, b:int) -> int:
    if a > b:
        return a
    else:
        return b
def mini(a:int, b:int) -> int:
    if a < b:
        return a
    else:
        return b
def ave(a:float, b:float) -> float:
    return (a + b)/2