-- select the score and the number of records for each score in the table `second_table` and order the results by score in descending order
select score, count(*) as number
from second_table
group by score
order by score DESC;