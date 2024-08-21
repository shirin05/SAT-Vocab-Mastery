import sqlite3
import csv

# Connect to the SQLite database (or create it if it doesn't exist)
print("Connecting to database...")
conn = sqlite3.connect('word_definition.db')
c = conn.cursor()

# needed print statements during debugging process
print("Dropping table if it exists...")
c.execute('DROP TABLE IF EXISTS words')

# Create the 'words' table with columns for word, definition, and difficulty
print("Creating table...")
c.execute('''
    CREATE TABLE IF NOT EXISTS words (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        definition TEXT NOT NULL,
        difficulty TEXT NOT NULL
    )
''')

# Open the CSV file and read the data
print("Reading CSV and inserting data...")
with open('word-list.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        c.execute('INSERT INTO words (word, definition, difficulty) VALUES (?, ?, ?)', (row[0], row[1], row[2]))


# Commit the changes and close the connection
print("Committing changes...")
conn.commit()
print("Closing connection...")
conn.close()


        