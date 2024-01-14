CREATE DATABASE IF NOT EXISTS inventory_management;

USE inventory_management;

CREATE TABLE IF NOT EXISTS t_product_item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL,
    category VARCHAR(50) NOT NULL,
    price VARCHAR(20) NOT NULL,
    last_updated_dt DATETIME NOT NULL,
    INDEX idx_category (category),
    INDEX idx_last_updated_dt (last_updated_dt)
);