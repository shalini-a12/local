import sqlite3

conn = sqlite3.connect("app_data.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS operators (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT
)
""")

# Insert a test operator
cursor.execute("INSERT INTO operators (username, password) VALUES (?, ?)", ("operator1", "1234"))

conn.commit()
conn.close()

print("Operator added successfully!")
