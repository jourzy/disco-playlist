-- drop database
-- DROP DATABASE db_disco_playlist_test;

-- Creating a new database
CREATE DATABASE IF NOT EXISTS db_disco_playlist_test;

-- Instructing program to use this database
USE db_disco_playlist_test;

-- a table to store the playlist
CREATE TABLE IF NOT EXISTS tbl_playlist (
	artist VARCHAR(100) NOT NULL,
    song VARCHAR(100) NOT NULL,
    votes INT NOT NULL DEFAULT 1,
    PRIMARY KEY (artist, song)
    );
    
DROP TABLE tbl_playlist;

INSERT INTO tbl_playlist
(artist, song)
VALUES
("Central Cee", "GBP"),
("Chappell Roan", "Pink Pony Club"),
("Chrystal", "The Days (NOTION Remix)"),
("Confidence Man & Sweely", "All My People"),
("Doechii", "DENIAL IS A RIVER"),
("Inhaler", "A Question Of You"),
("Kendrick Lamar & SZA", "Luther"),
("Lady Gaga", "Abracadabra"),
("Lola Young", "Messy"),
("PAWSA & The Adventures Of Stevie V", "Dirty Cash (Money Talks)");

-- increase votes to 2
UPDATE tbl_playlist
SET votes = 2
WHERE artist = "Doechii";

-- increase votes to 3
UPDATE tbl_playlist
SET votes = 3
WHERE artist = "Lola Young";

-- increase votes to 5
UPDATE tbl_playlist
SET votes = 5
WHERE artist = "Inhaler";

SELECT * FROM tbl_playlist;




