-- Write your query below
SELECT employee_id,
    CASE
        when Mod(employee_id,2)=0 OR name LIKE 'M%' THEN 0
        ELSE salary
    END as bonus

FROM employees
ORDER BY employee_id;