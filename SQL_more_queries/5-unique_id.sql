-- Create a table named `unique_id` with the following columns:
-- - `id`: an integer that cannot be NULL, has a default value of 1, and must be unique
-- - `name`: a string with a maximum length of 256 characters
CREATE TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT 1 UNIQUE, name VARCHAR(256));