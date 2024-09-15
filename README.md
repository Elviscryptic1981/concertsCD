# Concerts Database Project
This project is a Phase 3 Code Challenge for managing a Concert domain using raw SQL queries in Python. The database includes three tables: bands, venues, and concerts.

## Table of Contents
Setup
Database Schema
Sample Data
Methods
Concert Methods
Venue Methods
Band Methods
Testing
Contributing
License
## Setup
Clone the repository:
git clone (https://github.com/Elviscryptic1981/concertsCD.git)
cd concerts-db

Set up the database: Run the setup_db.py script to create the database and tables.
python3 setup_db.py

Insert sample data: Run the insert_data.py script to populate the tables with sample data.
python3 insert_data.py

## Database Schema
### bands Table:
id (INTEGER, PRIMARY KEY)
name (TEXT, NOT NULL)
hometown (TEXT, NOT NULL)
### venues Table:
id (INTEGER, PRIMARY KEY)
title (TEXT, NOT NULL)
city (TEXT, NOT NULL)
### concerts Table:
id (INTEGER, PRIMARY KEY)
band_id (INTEGER, NOT NULL, FOREIGN KEY)
venue_id (INTEGER, NOT NULL, FOREIGN KEY)
date (TEXT, NOT NULL)
### Sample Data
Sample data is inserted into the tables using the insert_data.py script. This includes sample bands, venues, and concerts.

## Methods
### Concert Methods
Concert.band(concert_id): Returns the Band instance for the given concert.
Concert.venue(concert_id): Returns the Venue instance for the given concert.
Concert.hometown_show(concert_id): Returns True if the concert is in the band’s hometown, False otherwise.
Concert.introduction(concert_id): Returns a string with the band’s introduction for the concert.
### Venue Methods
Venue.concerts(venue_id): Returns a collection of all concerts for the venue.
Venue.bands(venue_id): Returns a collection of all bands who performed at the venue.
Venue.concert_on(venue_id, date): Finds the first concert on the given date at the venue.
Venue.most_frequent_band(venue_id): Returns the band that has performed the most at the venue.
### Band Methods
Band.concerts(band_id): Returns a collection of all concerts the band has played.
Band.venues(band_id): Returns a collection of all venues the band has performed at.
Band.play_in_venue(band_id, venue_id, date): Creates a new concert for the band at the given venue on the given date.
Band.all_introductions(band_id): Returns an array of strings representing all the introductions for the band.
Band.most_performances(): Returns the band that has played the most concerts.
## Testing
To test the methods, you can run the concert_methods.py script and check the output.

python3 concert_methods.py

## Author
Elvis kimani elviskimani99@gmail.com

# License
This project is licensed under the MIT License.
