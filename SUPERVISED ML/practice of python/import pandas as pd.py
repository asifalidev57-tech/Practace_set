import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")

# Create cursor
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    marks INTEGER
)
""")

# Insert data
cur.execute(
    "INSERT INTO students (name, marks) VALUES (?, ?)",
    ("Asif", 95)
)

# Save changes
conn.commit()

# Read data
cur.execute("SELECT * FROM students")

# Fetch and display all rows
rows = cur.fetchall()

for row in rows:
    print(row)

# Close connection
conn.close()