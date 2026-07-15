# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM (
    SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM Employee
) ranked
WHERE salary_rank = 2;