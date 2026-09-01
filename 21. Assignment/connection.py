import sqlite3  
import os

def getConnection():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "student_details.sqlite3")
    
    con = sqlite3.connect(db_path, check_same_thread= False)
    con.execute("PRAGMA foreign_keys = ON")
    
    cur = con.cursor()
    return con, cur

def closeConnection(con, cur):
    cur.close()
    con.close()