-- ################# --
-- Dimensions Exploration 
-- ################# --

-- Retrieve a list of unique categories, subcategories, and products
SELECT DISTINCT 
    category, 
    sub_category, 
    product_name 
FROM gold.dim_products
ORDER BY category, sub_category, product_name;

-- ################# --
-- Date Range Exploration
-- ################# --

-- Determine the first and last order date and the total duration in months
SELECT 
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS last_order_date,
    date_diff('month', MIN(order_date), MAX(order_date)) AS order_range_months
FROM gold.fact_sales;

-- Find the youngest and oldest customer based on birthdate
SELECT
    MIN(birthdate) AS oldest_birthdate,
    DATEDIFF('year', MIN(birthdate), CURRENT_DATE) AS oldest_age,
    MAX(birthdate) AS youngest_birthdate,
    DATEDIFF('year', MAX(birthdate), CURRENT_DATE) AS youngest_age
FROM gold.dim_customer;
