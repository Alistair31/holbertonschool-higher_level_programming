-- count the number of TV shows for each genre and list the genres along with their corresponding show counts.
-- The result should be ordered by the number of shows in descending order.
SELECT tv_genres.name, COUNT(tv_shows.id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;