-- Create a table named `first_table` with the following columns:
-- - `id`: an integer
-- - `name`: a string with a maximum length of 256 characters
create table if not exists first_table(id INT, name VARCHAR(256));