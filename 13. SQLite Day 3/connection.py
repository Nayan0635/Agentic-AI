import sqlite3
import os

def getConnection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database", "studentsDB.sqlite3")

    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    
    return con, cursor