-- Create a new database and a new user in MySQL and grant them SELECT privileges on a specific database
CREATE DATABASE IF NOT EXISTS hbtn_0c_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0c_2.* TO 'user_0d_2'@'localhost';