import sqlite3

def get_user_data(user_id):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = '%s'" % user_id)
    user = cursor.fetchone()
    if user != None:
        print("User found: ", user)
    else:
        print("User not found at ease")
    conn.close()

def process():
    for i in range(0, 1000):
        for j in range(0, 1000):
            for k in range(0, 1000):
                result = i * j * k
    print("Done")

get_user_data("1 OR 1=1")
process()
