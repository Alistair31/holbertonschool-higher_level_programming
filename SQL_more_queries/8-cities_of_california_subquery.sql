-- Write a SQL query to list all the cities of California using the `cities` and `states` tables. The `cities` table has a foreign key `state_id` that references the `id` column in the `states` table. Use a subquery to find the `id` of California in the `states` table and then use that `id` to find the corresponding cities in the `cities` table.
SELECT * 
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');