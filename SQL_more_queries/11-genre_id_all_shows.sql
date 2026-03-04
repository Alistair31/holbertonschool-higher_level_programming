-- list all the TV shows along with their corresponding genre IDs.
-- If a TV show does not have a genre, the genre_id should be displayed as NULL.
-- Use a LEFT JOIN operation to combine the `tv_shows` and `tv_show_genres` tables based on the foreign key relationship between them.
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;