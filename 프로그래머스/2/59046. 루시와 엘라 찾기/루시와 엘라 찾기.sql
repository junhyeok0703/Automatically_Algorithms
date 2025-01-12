-- 코드를 입력하세요
# 쿼리를 작성하는 목표, 확인할 지표:
# 쿼리 계산 방법:
# 데이터의 기간:
# join key:
# 데이터 특징:

SELECT
 ANIMAL_ID,NAME,SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID