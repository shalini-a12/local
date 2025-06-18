import sqlite3

# Create/connect to the database
conn = sqlite3.connect("app_data.db")
cursor = conn.cursor()

# Create table for operators
cursor.execute("""
    CREATE TABLE IF NOT EXISTS operators (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
""")

# Insert two operator logins
cursor.execute("INSERT INTO operators (username, password) VALUES (?, ?)", ("operator1", "pass123"))
cursor.execute("INSERT INTO operators (username, password) VALUES (?, ?)", ("operator2", "pass456"))

conn.commit()
conn.close()

print("Database and operators created successfully!")

