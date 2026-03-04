-- Write a SQL query to list all the TV shows along with their corresponding genre IDs.
-- Use a JOIN operation to combine the `tv_shows` and `tv_show_genres` tables based on the foreign key relationship between them.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title;