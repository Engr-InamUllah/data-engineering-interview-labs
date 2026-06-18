-- Return each customer's latest order without correlated subqueries.
SELECT order_id, customer_id, order_date, amount
FROM (
  SELECT o.*, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC, order_id DESC) AS rn
  FROM orders o
) ranked WHERE rn = 1;

-- Seven-day rolling revenue.
SELECT order_date, daily_revenue,
       SUM(daily_revenue) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS revenue_7d
FROM (SELECT order_date, SUM(amount) daily_revenue FROM orders GROUP BY order_date) daily;