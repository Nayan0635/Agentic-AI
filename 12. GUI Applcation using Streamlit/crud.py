import sqlite3
import pandas as pd

# Connection Object
def create_connection():
    return sqlite3.connect("./database/usersDB.sqlite3", check_same_thread=False)

# Accessing The Database
def get_cursor(con):
    return con.cursor()

def addNewUser(name: str, email: str) -> str:
    con = create_connection()
    cursor = get_cursor(con)
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        con.commit()
        rows = cursor.rowcount
        if rows == 1:
            return 'User successfully Registered with Us'
        else:
            return 'Error inserting new user'
    except sqlite3.Error as e:
        return f'Error inserting new user: {e}'
    finally:
        con.close()

def getAllUsers():
    con = create_connection()
    try:
        df = pd.read_sql_query("SELECT name, email, created FROM users", con)
        return df
    except sqlite3.Error as e:
        return f'Error retrieving users: {e}'
    finally:
        con.close()