-- 코드를 입력하세요
SELECT 
  EXTRACT(hour from DATETIME) as HOUR,
  COUNT(*) as COUNT
FROM 
  ANIMAL_OUTS
WHERE 
  EXTRACT(hour from DATETIME) >=9 and EXTRACT(hour from DATETIME) < 20
GROUP BY 
  EXTRACT(hour from DATETIME)
ORDER BY 
  EXTRACT(hour from DATETIME) asc
