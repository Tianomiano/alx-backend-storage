-- SQL script that creates a table users with these attributes 
-- id, email, name and country enumeration US,CO, TN DEFAULT US
CREATE TABLE IF NOT EXISTS users (
        id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
        email varchar(255) NOT NULL UNIQUE,
        name varchar(255),
        country ENUM('US', 'CO', 'TN' ) NOT NULL DEFAULT 'US'
);
