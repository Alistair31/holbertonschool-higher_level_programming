-- select the score and the number of records for each score in the table `second_table` and order the results by score in descending order
SELECT score, count(*) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;