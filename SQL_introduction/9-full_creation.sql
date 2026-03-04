-- Create a table named `second_table` with the following columns:
-- - `id`: an integer
-- - `name`: a string with a maximum length of 256 characters
-- - `score`: an integer
create table if not exists second_table(id INT, name VARCHAR(256), score INT);
insert into second_table(`id`, `name`, `score`)
values
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);