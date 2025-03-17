import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('all_names_count.db')
cursor = conn.cursor()

# Open the text file and read its contents
with open("query_all_names_count.txt", 'w+') as file:
    # Query the database for the counts of the names "John" and "Jasmine"
    cursor.execute('''
                SELECT name, count FROM all_names_count WHERE name IS "Lucy"
                ''')
    # Write the results to a text file
    for row in cursor:
        line = ",".join([str(row[0]), str(row[1])])
        print(line)
        file.write(line)

file.close()
print("File closed.")

# Commit the transaction and close the connection
conn.commit()
conn.close()

print("Query extracted successfully.")