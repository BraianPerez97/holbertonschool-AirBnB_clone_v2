-- Setting MySQL server, creates user and applies access


CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
SET PASSWORD FOR 'hbnb_test'@'localhost' = 'hbnb_dev_pwd'
GRANT ALL PRIVILEGES ON 'hbnb_dev_db'.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';