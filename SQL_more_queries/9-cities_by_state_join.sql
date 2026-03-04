-- Write a SQL query to list all the cities along with their corresponding state names.
-- Use a JOIN operation to combine the `cities` and `states` tables based on the foreign key relationship between them.
SELECT cities.id, cities.name, states.name AS state_name
FROM cities
JOIN states ON cities.state_id = states.id;