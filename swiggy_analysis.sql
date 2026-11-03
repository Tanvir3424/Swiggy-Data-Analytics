USE swiggy_analysis;

-- SELECT
--     restaurant_name,
--     cuisine,
--     rating,
--     number_of_ratings,
--     average_price,
--     area
-- FROM swiggy_restaurants
-- WHERE rating IS NOT NULL
-- ORDER BY rating DESC
-- LIMIT 10;

-- SELECT
--     area,
--     COUNT(*) AS total_restaurants
-- FROM swiggy_restaurants
-- WHERE area IS NOT NULL
-- GROUP BY area
-- ORDER BY total_restaurants DESC
-- LIMIT 10;

-- SELECT
--     cuisine,
--     COUNT(*) AS total_restaurants
-- FROM swiggy_restaurants
-- WHERE cuisine IS NOT NULL
-- GROUP BY cuisine
-- ORDER BY total_restaurants DESC
-- LIMIT 10;

-- SELECT
--     cuisine,
--     ROUND(AVG(average_price), 2) AS avg_price,
--     COUNT(*) AS total_restaurants
-- FROM swiggy_restaurants
-- WHERE cuisine IS NOT NULL
-- AND average_price IS NOT NULL
-- GROUP BY cuisine
-- HAVING COUNT(*) >= 100
-- ORDER BY avg_price DESC
-- LIMIT 10;

-- SELECT
--     pure_veg,
--     COUNT(*) AS total_restaurants,
--     ROUND(AVG(average_price), 2) AS avg_price
-- FROM swiggy_restaurants
-- WHERE pure_veg IS NOT NULL
-- GROUP BY pure_veg
-- ORDER BY total_restaurants DESC;

-- SELECT
--     number_of_offers,
--     COUNT(*) AS total_restaurants,
--     ROUND(AVG(average_price), 2) AS avg_price
-- FROM swiggy_restaurants
-- WHERE number_of_offers IS NOT NULL
-- GROUP BY number_of_offers
-- ORDER BY number_of_offers;

SELECT
    area,
    ROUND(AVG(rating), 2) AS avg_rating,
    COUNT(*) AS total_restaurants
FROM swiggy_restaurants
WHERE area IS NOT NULL
AND rating IS NOT NULL
GROUP BY area
HAVING COUNT(*) >= 100
ORDER BY avg_rating DESC
LIMIT 10;