import sqlite3


conn   = sqlite3.connect('db_name.db')
cursor = conn.cursor()

# database table creation
cursor.execute(f"CREATE TABLE IF NOT EXISTS key_table(id INTEGER PRIMARY KEY NOT NULL, key_name TEXT UNIQUE, key_value TEXT)")


# insert data into database
values   = ('a', 1)
db_query = f"INSERT OR IGNORE INTO key_table(key_name, key_value) VALUES (?, ?)"
cursor.execute(db_query, values)
conn.commit()

# read data from database
cursor.execute('SELECT * FROM key_table')
result = cursor.fetchall()
print(result)