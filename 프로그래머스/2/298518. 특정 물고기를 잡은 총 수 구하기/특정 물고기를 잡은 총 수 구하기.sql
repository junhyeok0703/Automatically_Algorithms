-- 코드를 작성해주세요
SELECT COUNT(ID) as FISH_COUNT
FROM FISH_INFO FI
INNER JOIN FISH_NAME_INFO FNI
ON FI.FISH_TYPE = FNI.FISH_TYPE
WHERE FISH_NAME IN ('BASS','SNAPPER')
