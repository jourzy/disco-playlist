-- Creating a new database
CREATE DATABASE IF NOT EXISTS db_disco_playlist;

-- Instructing program to use this database
USE db_disco_playlist;

-- a table to store artists added to the database
CREATE TABLE IF NOT EXISTS tbl_artists (
	artist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    artist_name VARCHAR(100) NOT NULL
);

-- a table to store songs added to the database
CREATE TABLE IF NOT EXISTS tbl_songs (
	song_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    song_name VARCHAR(100) NOT NULL,
    song_artist_id INT NOT NULL,
	-- add foreign key constraint for song_artist_id
	CONSTRAINT fk_song_artist_id
	FOREIGN KEY (song_artist_id)
	REFERENCES tbl_artists (artist_id)
);

-- a table to store the playlist
CREATE TABLE IF NOT EXISTS tbl_playlist (
	playlist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    playlist_song_id INT NOT NULL,
    playlist_artist_id INT NOT NULL,
    votes INT NOT NULL DEFAULT 1,
	-- add foreign key constraint for playlist_song_id
	CONSTRAINT fk_playlist_song_id
	FOREIGN KEY (playlist_song_id)
	REFERENCES tbl_songs (song_id),
	-- add foreign key constraint for playlist_artist_id
	CONSTRAINT fk_playlist_artist_id
	FOREIGN KEY (playlist_artist_id)
	REFERENCES tbl_songs (song_artist_id)
);

