import sqlite3

# Connecting to SQLite database
conn = sqlite3.connect('new.db')

# Creating a cursor object
cursor = conn.cursor()

# Creating a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )
''')

# Inserting data into the table
cursor.execute('''
    INSERT INTO users (name, age, city)
    VALUES (?, ?, ?)
''', ('Aarati', 23, 'Pokhara'))

# Committing the transaction
conn.commit()

# Querying the data to verify the insertion
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

print("Data in the 'users' table:")
for row in rows:
    print(row)

# Closing the connection
conn.close()
