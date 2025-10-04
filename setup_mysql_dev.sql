<<<<<<< HEAD
-- script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
=======
-- MySQL setup for development environment
-- Creates database, user, and grants required privileges

CREATE DATABASE IF NOT EXISTS hbnb_dev_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';

GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;


>>>>>>> c5c69c3b281ca80047e1f7969e0cd1ee2d9e23eb
