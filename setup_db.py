import sqlite3

conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Drop tables if they exist
cursor.execute('DROP TABLE IF EXISTS bands')
cursor.execute('DROP TABLE IF EXISTS venues')
cursor.execute('DROP TABLE IF EXISTS concerts')

# Create tables
cursor.execute('''
CREATE TABLE bands (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    hometown TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE venues (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    city TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE concerts (
    id INTEGER PRIMARY KEY,
    band_id INTEGER NOT NULL,
    venue_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (band_id) REFERENCES bands(id),
    FOREIGN KEY (venue_id) REFERENCES venues(id)
)
''')

conn.commit()
conn.close()
