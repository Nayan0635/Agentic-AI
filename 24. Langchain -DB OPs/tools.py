from langchain_core.tools import tool
from connection import *
import json

@tool
def addNewUser(name:str,email:str)->str:
    '''adding new user by accepting name & email from users prompt into the Sqlite3 Database'''
    (con,cur) = getConnection()
    cur.execute("insert into users(name,email)values(?,?)",(name,email))
    con.commit()
    rows = cur.rowcount
    #close the Database connection
    closeConnection(con, cur)

    if rows == 1:
        return 'User Added Successfully.'
    else:
        return 'Unable to SignUp User.'

@tool 
def getUser(user_id:int)->dict:
    '''getting specific user details from the sqlite3 database'''
    (con,cur) = getConnection()
    cur.execute("select * from users where user_id=?",(user_id,))
    row =cur.fetchone()
    #close the Database connection
    closeConnection(con, cur)

    if row:
     return {
        "name":row[1],
        "email":row[2]
     }
    else:
        return {"message":"No such user found"}

@tool
def getAllUsers()->str:
    '''getting & displaying all users records from the Sqlite3 Databbase'''
    (con,cur) = getConnection()
    cur.execute("select * from users")
    rows =cur.fetchall()
    #close the Database connection
    closeConnection(con, cur)
    users = [] #empty list
    for row in rows:
        users.append({
            "name":row[1],
            "email":row[2]
        })
    return json.dumps(users,indent=1)

@tool
def deleteUser(uid:int)->str:
    '''deleting user from database'''
    (con,cur)= getConnection()
    cur.execute("delete from users where user_id=?",(uid,))
    con.commit()
    rows =cur.rowcount
    closeConnection(con, cur)
    if rows ==1:
        return 'One user deleted successfully'
    else:
        return 'Unable to delete.'
    
@tool
def updateUser(uid: int, name: str = "", email: str = "") -> str:
    '''Update an existing user's name or email.
    Use this tool when the user asks to update, change, modify,
    or edit an existing user's information.
    Requires the user's user_id.'''
    (con, cur) = getConnection()
    cur.execute(
        "select name, email from users where user_id=?",
        (uid,)
    )
    user = cur.fetchone()
    if not user:
        closeConnection(con, cur)
        return "No such user found."
    if not name:
        name = user[0]
    if not email:
        email = user[1]
    cur.execute(
        "update users set name=?, email=? where user_id=?",
        (name, email, uid)
    )
    con.commit()
    rows = cur.rowcount
    closeConnection(con, cur)
    if rows == 1:
        return "User Profile successfully Updated"
    else:
        return "Unable to Update User Profile"