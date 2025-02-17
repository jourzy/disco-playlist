-- DROP DATABASE db_disco_playlist;

-- Creating a new database
CREATE DATABASE IF NOT EXISTS db_disco_playlist;

-- Instructing program to use this database
USE db_disco_playlist;

-- a table to store the playlist
CREATE TABLE IF NOT EXISTS tbl_playlist (
	artist VARCHAR(100) NOT NULL,
    song VARCHAR(100) NOT NULL,
    votes INT NOT NULL DEFAULT 1,
    PRIMARY KEY (artist, song)
    );