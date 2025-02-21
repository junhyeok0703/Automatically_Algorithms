SELECT 
    ECOLI_DATA.ID,
    COALESCE(COUNT(Children.PARENT_ID),0) AS CHILD_COUNT
FROM 
    ECOLI_DATA
LEFT JOIN 
    ECOLI_DATA AS Children
    ON ECOLI_DATA.ID = Children.PARENT_ID
GROUP BY ECOLI_DATA.ID
ORDER BY ECOLI_DATA.ID