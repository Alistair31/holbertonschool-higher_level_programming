-- Create a table named `id_not_null` with the following columns:
-- - `id`: an integer that cannot be NULL and has a default value of 1
-- - `name`: a string with a maximum length of 256 characters
CREATE TABLE IF NOT EXISTS id_not_null(id INT NOT NULL DEFAULT 1, name VARCHAR(256));