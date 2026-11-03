from connection import *
def addNewPost(title:str,desc:str)->str:
    '''adding new Post to Sqlite3 Database asking title , description from the user as a prompt'''
    (con,cur) = getConnection()
    cur.execute("insert into posts(title,description)values(?,?)",(title,desc))
    rows = cur.rowcount
    con.commit()
    closeConnection(con, cur)
    if rows == 1:
        return {"message":"New Post Added Successfully"}
    else:
        return {"error":"Unble to Add a New Post !"}
    
def getAllPosts():
    (con,cur) = getConnection()
    cur.execute("select * from posts")
    rows = cur.fetchall()
    closeConnection(con, cur)
    posts =[] #empty list
    for row in rows:
        posts.append({
            "post_id":row[0],
            "title":row[1],
            "description":row[2],
            "created":row[3]
        })
    return posts


def getPost(post_id: int):
    """Get a single post from the database using its post ID."""
    con, cur = getConnection()

    cur.execute(
        "SELECT * FROM posts WHERE post_id = ?",
        (post_id,)
    )
    row = cur.fetchone()

    closeConnection(con, cur)

    if row is None:
        return {"error": "Post not found"}

    return {
        "post_id": row[0],
        "title": row[1],
        "description": row[2],
        "created": row[3]
    }


def updatePost(title: str, desc: str, post_id: int):
    """Update the title and description of an existing post."""
    con, cur = getConnection()

    cur.execute(
        "UPDATE posts SET title = ?, description = ? WHERE post_id = ?",
        (title, desc, post_id)
    )
    rows = cur.rowcount

    con.commit()
    closeConnection(con, cur)

    if rows == 1:
        return {"message": "Post updated successfully"}
    return {"error": "Post not found or unable to update"}


def deletePost(post_id: int):
    """Delete a post from the database using its post ID."""
    con, cur = getConnection()

    cur.execute(
        "DELETE FROM posts WHERE post_id = ?",
        (post_id,)
    )
    rows = cur.rowcount

    con.commit()
    closeConnection(con, cur)

    if rows == 1:
        return {"message": "Post deleted successfully"}
    return {"error": "Post not found or unable to delete"}

