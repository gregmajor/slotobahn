-- Schema for the database.

-- Create the orders table
CREATE TABLE IF NOT EXISTS Orders (
  id          INT PRIMARY KEY,
  order_year  INT,
  order_month INT,
  order_count INT
);

-- SQL Query to get the seed data from production
--   SELECT YEAR([LastModifiedDateTime]) AS 'Year',
--          CONVERT(CHAR(3), [LastModifiedDateTime], 0) AS 'MonthName',
-- 		 COUNT(*) AS 'OrderCount'
--     FROM [dbo].[Orders]
-- GROUP BY YEAR([LastModifiedDateTime]), MONTH([LastModifiedDateTime]), CONVERT(CHAR(3), [LastModifiedDateTime], 0)
-- ORDER BY YEAR([LastModifiedDateTime]), MONTH([LastModifiedDateTime]), CONVERT(CHAR(3), [LastModifiedDateTime], 0)

-- Seed the orders table for 2015
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 1, 1327) WHERE NOT EXISTS(SELECT 1 FROM Orders WHERE order_year = 2015 AND order_month = 1);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 2, 1026) WHERE NOT EXISTS(SELECT 1 FROM Orders WHERE order_year = 2015 AND order_month = 2);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 3, 933) WHERE NOT EXISTS(SELECT 1 FROM Orders WHERE order_year = 2015 AND order_month = 3);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 4, 0) WHERE NOT EXISTS(SELECT 1 FROM Orders WHERE order_year = 2015 AND order_month = 4);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 5, 0) WHERE NOT EXISTS(SELECT 1 FROM Orders WHERE order_year = 2015 AND order_month = 5);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 6, 0) WHERE NOT EXISTS(SELECT 1 FROM Orders WHERE order_year = 2015 AND order_month = 6);
