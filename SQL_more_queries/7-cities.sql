-- Create a database named `hbtn_0d_usa` if it does not already exist, and then create a table named `cities` with the following columns:
-- - `id`: an integer that cannot be NULL and auto-increments with each new entry
-- - `state_id`: an integer that cannot be NULL and is a foreign key referencing the `id` column of the `states` table
-- - `name`: a string with a maximum length of 256 characters that cannot be NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);