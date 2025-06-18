import sqlite3

conn = sqlite3.connect("app_data.db")
cursor = conn.cursor()

# Create product table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        quantity INTEGER,
        price REAL
    )
""")

conn.commit()
conn.close()
print("Product table created successfully!")
