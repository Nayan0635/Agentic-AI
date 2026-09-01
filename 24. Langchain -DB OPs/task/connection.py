import sqlite3

def getConnection():
    con = sqlite3.connect("./database.sqlite3",check_same_thread=False)
    con.execute("PRAGMA foreign_key = ON")
    cursor = con.cursor()
    return (con,cursor)

def closeConnection(con, cur):
    cur.close()
    con.close()
