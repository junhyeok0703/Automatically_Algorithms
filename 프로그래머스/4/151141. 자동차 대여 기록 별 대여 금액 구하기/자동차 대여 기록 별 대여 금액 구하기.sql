WITH TRUCK_RENTAL AS (
    SELECT
        h.history_id,
        c.daily_fee,
        DATEDIFF(h.end_date, h.start_date) + 1 AS rent_days          -- 실제 대여 일수
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS h
    JOIN CAR_RENTAL_COMPANY_CAR              AS c  ON h.car_id = c.car_id
    WHERE c.car_type = '트럭'
),
TRUCK_DISCOUNT AS (
    /* 기간 구간별 최소 일수와 할인율 */
    SELECT
        CASE duration_type
              WHEN '7일 이상'  THEN  7
              WHEN '30일 이상' THEN 30
              WHEN '90일 이상' THEN 90
        END                                AS min_days,
        discount_rate
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    WHERE car_type = '트럭'
)
SELECT
    r.history_id,
    ROUND(( r.daily_fee * r.rent_days
      * (100 - IFNULL(                     -- 기간에 맞는 할인율(없으면 0)
           ( SELECT d.discount_rate
             FROM  TRUCK_DISCOUNT d
             WHERE r.rent_days >= d.min_days
             ORDER BY d.min_days DESC      -- 가장 큰 min_days = 가장 정확한 구간
             LIMIT 1
           ), 0 )
        ) / 100 ),0)                          AS FEE
FROM TRUCK_RENTAL r
ORDER BY FEE DESC, r.history_id DESC;
