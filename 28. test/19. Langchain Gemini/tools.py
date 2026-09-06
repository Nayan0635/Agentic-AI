from langchain_core.tools import tool
from connection import getConnection, closeConnection
import json

@tool
def calculator(expression: str) -> str:
    """Calculate mathematical expressions.
    Use this tool when the user asks to perform arithmetic calculations, 
    such as 'Calculate 250 * 45' or '100 + 50'.
    
    Args:
        expression: A mathematical expression string, e.g. '250 * 45'.
    """
    try:
        allowed_chars = "0123456789+-*/(). %"
        cleaned_expr = str(expression).strip()
        if not all(c in allowed_chars for c in cleaned_expr):
            return "Error: Invalid characters in mathematical expression."
        
        result = eval(cleaned_expr, {"__builtins__": None}, {})
        return f"Calculation Result: {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

@tool
def sqlite_query(query: str) -> str:
    """Execute SQL queries on the SQLite database.
    Use this tool to execute SQL queries on the students database table (columns: student_id, name, email).
    
    Args:
        query: SQL query string to execute.
    """
    con, cur = getConnection()
    try:
        cur.execute(query)
        if query.strip().upper().startswith("SELECT") or query.strip().upper().startswith("PRAGMA"):
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description] if cur.description else []
            result = [dict(zip(columns, row)) for row in rows]
            return json.dumps(result, indent=2)
        else:
            con.commit()
            return f"Query executed successfully. Affected rows: {cur.rowcount}"
    except Exception as e:
        return f"Database error: {str(e)}"
    finally:
        closeConnection(con, cur)

@tool
def find_student_by_name(name: str) -> str:
    """Find student(s) from the database by name.
    Use this tool when searching for a student by name, 
    such as 'Find student Rahul from the database?'.
    
    Args:
        name: Name or partial name of the student to find.
    """
    con, cur = getConnection()
    try:
        cur.execute("SELECT student_id, name, email FROM students WHERE LOWER(name) LIKE LOWER(?)", (f"%{name}%",))
        rows = cur.fetchall()
        if not rows:
            return f"No student found with name '{name}'."
        students = [{"student_id": r[0], "name": r[1], "email": r[2]} for r in rows]
        return json.dumps(students, indent=2)
    except Exception as e:
        return f"Error finding student: {str(e)}"
    finally:
        closeConnection(con, cur)

@tool
def find_student_by_id(student_id: int) -> str:
    """Find a student record from the database by student_id.
    
    Args:
        student_id: ID of the student.
    """
    con, cur = getConnection()
    try:
        cur.execute("SELECT student_id, name, email FROM students WHERE student_id = ?", (student_id,))
        row = cur.fetchone()
        if row:
            return json.dumps({"student_id": row[0], "name": row[1], "email": row[2]}, indent=2)
        return f"No student found with ID {student_id}."
    except Exception as e:
        return f"Error finding student: {str(e)}"
    finally:
        closeConnection(con, cur)

@tool
def show_all_students() -> str:
    """Show all student records from the database."""
    con, cur = getConnection()
    try:
        cur.execute("SELECT student_id, name, email FROM students")
        rows = cur.fetchall()
        if not rows:
            return "No students found in database."
        students = [{"student_id": r[0], "name": r[1], "email": r[2]} for r in rows]
        return json.dumps(students, indent=2)
    except Exception as e:
        return f"Error fetching students: {str(e)}"
    finally:
        closeConnection(con, cur)

@tool
def add_student(name: str, email: str) -> str:
    """Add a new student to the database with name and email.
    
    Args:
        name: Student's name.
        email: Student's email address.
    """
    con, cur = getConnection()
    try:
        cur.execute("INSERT INTO students (name, email) VALUES (?, ?)", (name, email))
        con.commit()
        return f"Successfully added student '{name}' with student_id {cur.lastrowid}."
    except Exception as e:
        return f"Error adding student: {str(e)}"
    finally:
        closeConnection(con, cur)

@tool
def update_student(student_id: int, name: str = None, email: str = None) -> str:
    """Update an existing student's name or email.
    
    Args:
        student_id: Student ID to update.
        name: Optional new name.
        email: Optional new email.
    """
    con, cur = getConnection()
    try:
        cur.execute("SELECT name, email FROM students WHERE student_id = ?", (student_id,))
        row = cur.fetchone()
        if not row:
            return f"Student with ID {student_id} does not exist."
        
        new_name = name if name else row[0]
        new_email = email if email else row[1]
        
        cur.execute("UPDATE students SET name = ?, email = ? WHERE student_id = ?", (new_name, new_email, student_id))
        con.commit()
        return f"Successfully updated student ID {student_id}."
    except Exception as e:
        return f"Error updating student: {str(e)}"
    finally:
        closeConnection(con, cur)

@tool
def delete_student(student_id: int) -> str:
    """Delete a student record by student_id.
    
    Args:
        student_id: Student ID to delete.
    """
    con, cur = getConnection()
    try:
        cur.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        con.commit()
        if cur.rowcount > 0:
            return f"Successfully deleted student ID {student_id}."
        return f"No student found with ID {student_id}."
    except Exception as e:
        return f"Error deleting student: {str(e)}"
    finally:
        closeConnection(con, cur)