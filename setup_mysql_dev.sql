-- script that prepares a MySQL server for the project:
-- Create the database if it doesn't exist
-- Create the database if it doesn't exist with the specified character set and collation
CREATE DATABASE IF NOT EXISTS hbnb_dev_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;

