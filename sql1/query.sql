-- 1. Top 5 Funds by AUM
SELECT *
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Funds with Expense Ratio Less Than 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 3. Top Rated Funds
SELECT *
FROM fact_performance
ORDER BY morningstar_rating DESC
LIMIT 10;

-- 4. Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 5. Total Transaction Amount
SELECT SUM(amount_inr)
FROM fact_transactions;