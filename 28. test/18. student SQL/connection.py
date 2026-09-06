import sqlite3
import os

def getConnection():
    db_path = os.path.join(os.path.dirname(__file__), "student.db")
    con = sqlite3.connect(db_path, check_same_thread=False)
    cur = con.cursor()
    return con, cur

def closeConnection(con, cur):
    cur.close()
    con.close() #know the order close cursor first then conncetion..