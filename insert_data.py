import sqlite3

conn = sqlite3.connect('concerts.db')
cursor = conn.cursor()

# Insert data into bands
cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Band A', 'Hometown A')")
cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Band B', 'Hometown B')")

# Insert data into venues
cursor.execute("INSERT INTO venues (title, city) VALUES ('Venue X', 'City X')")
cursor.execute("INSERT INTO venues (title, city) VALUES ('Venue Y', 'City Y')")

# Insert data into concerts
cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-09-01')")
cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-09-02')")

conn.commit()
conn.close()
