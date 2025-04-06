-- Create the database
CREATE DATABASE attendance_system;

-- Use the database
USE attendance_system;

-- Table to store user details
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    rfid_tag VARCHAR(50) UNIQUE,
    face_id VARCHAR(100) UNIQUE
);

-- Table to log attendance
CREATE TABLE attendance_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    check_in_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    status ENUM('Present', 'Late', 'Absent') DEFAULT 'Present',
    method ENUM('RFID', 'Face') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Optional: Pre-populate a few users
INSERT INTO users (name, email, rfid_tag, face_id)
VALUES 
('Alice Johnson', 'alice@example.com', 'A1B2C3D4', 'face_001'),
('Bob Smith', 'bob@example.com', 'X9Y8Z7W6', 'face_002');
