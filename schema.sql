-- Schema for the database.

-- Create the orders table
CREATE TABLE IF NOT EXISTS Orders (
  id          INT PRIMARY KEY,
  order_year  INT,
  order_month INT,
  order_count INT
);
