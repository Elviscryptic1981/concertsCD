import sqlite3

class Concert:
    @staticmethod
    def band(concert_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bands WHERE id = (SELECT band_id FROM concerts WHERE id = ?)", (concert_id,))
        band = cursor.fetchone()
        conn.close()
        return band

# Test the method
concert_band = Concert.band(1)
print(concert_band)
