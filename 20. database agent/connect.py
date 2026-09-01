import sqlite3
import os

def getConnection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "students.sqlite3") #know about it
    
    con = sqlite3.connect(db_path, check_same_thread= False)
    cur = con.cursor()
    
    return con, cur

def closeConnection(con, cur):
    cur.close()
    con.close() #know the order close cursor first then conncetion..