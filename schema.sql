-- Schema for the database.

-- Create the orders table
CREATE TABLE IF NOT EXISTS Orders (
  id          INT PRIMARY KEY,
  order_year  INT NOT NULL,
  order_month INT NOT NULL,
  order_count INT NOT NULL,
  UNIQUE (order_year, order_month) ON CONFLICT IGNORE
);

-- SQL Query to get the seed data from production
--   SELECT YEAR([LastModifiedDateTime]) AS 'Year',
--          CONVERT(CHAR(3), [LastModifiedDateTime], 0) AS 'MonthName',
-- 		 COUNT(*) AS 'OrderCount'
--     FROM [dbo].[Orders]
-- GROUP BY YEAR([LastModifiedDateTime]), MONTH([LastModifiedDateTime]), CONVERT(CHAR(3), [LastModifiedDateTime], 0)
-- ORDER BY YEAR([LastModifiedDateTime]), MONTH([LastModifiedDateTime]), CONVERT(CHAR(3), [LastModifiedDateTime], 0)

-- 2014	Jun	1968
-- 2014	Jul	3028
-- 2014	Aug	1261
-- 2014	Sep	1021
-- 2014	Oct	1187
-- 2014	Nov	1381
-- 2014	Dec	969
-- 2015	Jan	1327
-- 2015	Feb	1026
-- 2015	Mar	933

-- Seed the orders table
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2014, 6, 1968);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2014, 7, 3028);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2014, 8, 1261);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2014, 9, 1021);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2014, 10, 1187);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2014, 11, 1381);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2014, 12, 969);

INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 1, 1327);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 2, 1026);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 3, 933);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 4, 0);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 5, 0);
INSERT INTO Orders (order_year, order_month, order_count) VALUES(2015, 6, 0);
