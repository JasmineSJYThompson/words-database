import sqlite3

# Define the path to your text file
text_file_path = 'all_names_count_head.txt'

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('all_names_count.db')
cursor = conn.cursor()

# Create a table to store words and their counts
cursor.execute('''
    CREATE TABLE IF NOT EXISTS all_names_count (
        name TEXT PRIMARY KEY,
        count INTEGER
    )
''')

# Open the text file and read its contents
with open(text_file_path, 'r') as file:
    for line in file:
        # Split each line into word and count
        word, count = line.strip().split(",")
        count = int(count)  # Convert count to integer

        # Insert the word and count into the database
        cursor.execute('''
            INSERT OR REPLACE INTO all_names_count (name, count)
            VALUES (?, ?)
        ''', (word, count))

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Database created and data inserted successfully.")