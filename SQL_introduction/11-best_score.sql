-- select the score and name of all records in the table `second_table` where the score is higher than or equal to 10
SELECT score, name
FROM second_table
WHERE score >= 10 
ORDER BY score DESC;