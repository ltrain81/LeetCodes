# Write your MySQL query statement below
select E.name as Employee
from Employee as E
where E.salary > 
(
    select B.salary
    from Employee as B
    where E.managerId = B.id
)