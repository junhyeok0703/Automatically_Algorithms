-- 코드를 입력하세요
SELECT
    YEAR(OS.sales_date) AS YEAR,
    MONTH(OS.sales_date) AS MONTH,
    UI.gender AS GENDER,
    COUNT(DISTINCT UI.user_id) AS USERS
FROM USER_INFO AS UI
JOIN ONLINE_SALE AS OS
ON UI.USER_ID = OS.USER_ID
WHERE UI.gender IS NOT NULL
GROUP BY YEAR(OS.sales_date),MONTH(OS.sales_date),UI.gender
ORDER BY YEAR(OS.sales_date),MONTH(OS.sales_date),UI.gender