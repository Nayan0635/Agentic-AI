import sqlite3

def getConnection():
    con = sqlite3.connect("./usersDB.sqlite3",check_same_thread=False)
    cursor = con.cursor()
    return (con,cursor)

def closeConnection(con, cur):
    cur.close()
    con.close()
