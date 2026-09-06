import sqlite3
import os

def getConnection():
    db_path = os.path.join(os.path.dirname(__file__), "student.sqlite3")
    con = sqlite3.connect(db_path, check_same_thread=False)
    cur = con.cursor()
    return con, cur

def closeConnection(con, cur):
    if cur:
        cur.close()
    if con:
        con.close()