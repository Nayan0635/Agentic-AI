# import sqlite3

# def getConnection():
#     con = sqlite3.connect("./studentsDB.sqlite3",check_same_thread=False)
#     cursor = con.cursor()
#     return (con,cursor)
import sqlite3
import os

def getConnection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "studentsDB.sqlite3")

    con = sqlite3.connect(db_path)
    cursor = con.cursor()

    return con, cursor