CREATE DATABASE IF NOT EXISTS inventory_management;

USE inventory_management;

CREATE TABLE IF NOT EXISTS t_product_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE,
    category VARCHAR(50),
    price VARCHAR(20),
    last_updated_dt DATETIME,
    INDEX idx_last_updated_dt (last_updated_dt)
);