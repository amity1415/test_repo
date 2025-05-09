import sqlite3

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # ❌ SQL Injection risk
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    # ❌ Insecure plain-text password check
    user = cursor.fetchone()
    if user != None:
        print("Welcome", username)
    else:
        print("Access denied")
    
    conn.close()

# ❌ Hardcoded credentials
authenticate_user("admin", "admin123")
