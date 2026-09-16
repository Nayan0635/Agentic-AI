import sqlite3

def getConnection():
    con = sqlite3.connect("./studentDB.sqlite3",check_same_thread=False)
    cursor = con.cursor()
    return (con,cursor)
