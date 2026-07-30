-- Create the user_0d_1 and add all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1-pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
