CREATE DATABASE IF NOT EXISTS library;
USE library;

CREATE TABLE IF NOT EXISTS publishers (
    publisherID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    name VARCHAR(64),
    address VARCHAR(128),
    amountOfBooks INT,
    founderDate DATE
);

CREATE TABLE IF NOT EXISTS versions (
    versionID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    publisherID INT,
    bookID INT
);

CREATE TABLE IF NOT EXISTS books (
   bookID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
   title VARCHAR(64),
   category VARCHAR(64),
   releaseDate DATE,
   authorID INT
);

CREATE TABLE IF NOT EXISTS authorGroups (
    groupID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    authorID INT,
    bookID INT
);

CREATE TABLE IF NOT EXISTS authors (
    authorID INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
    email VARCHAR(64),
    address VARCHAR(128),
    birthday DATE,
    mobileNumber INT
);