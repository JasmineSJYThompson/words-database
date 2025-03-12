import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('all_names_count.db')
cursor = conn.cursor()

# Query to select all data from the WordCount table
cursor.execute('SELECT name, count FROM all_names_count')

# Fetch all rows from the executed query
rows = cursor.fetchall()

# Iterate over the rows and print each word and its count
for row in rows[0:10]:
    name, count = row
    print(f'{name},{count}')

# Close the connection
conn.close()