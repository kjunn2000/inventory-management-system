-- Create the database
CREATE DATABASE IF NOT EXISTS inventory_management;

-- Switch to the database
USE inventory_management;

-- Create the table
CREATE TABLE IF NOT EXISTS t_product_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(50),
    price VARCHAR(20),
    last_updated_dt DATETIME
);