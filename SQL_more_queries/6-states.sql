-- Create a database named `hbtn_0d_usa` if it does not already exist, and then create a table named `states` with the following columns:
-- - `id`: an integer that cannot be NULL, must be unique, and auto-increments with each new entry
-- - `name`: a string with a maximum length of 256 characters that cannot be NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states ( id INT NOT NULL UNIQUE AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id));