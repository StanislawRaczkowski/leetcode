# Write your MySQL query statement below
SELECT max(num) AS num
FROM MyNumbers
WHERE num IN
    (SELECT IF(COUNT(num) = 1, num, NULL)
    FROM MyNumbers
    GROUP BY 
    num)




