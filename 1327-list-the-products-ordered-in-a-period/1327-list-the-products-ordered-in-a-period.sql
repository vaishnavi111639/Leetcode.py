# Write your MySQL query statement below
WITH full_table AS( 
    SELECT product_name, SUM(unit) AS unit
    FROM Products p
    JOIN Orders o USING(product_id)
    WHERE order_date LIKE '2020-02-__'
    GROUP BY product_name
)
SELECT product_name,unit
FROM full_table 
WHERE unit>=100
;