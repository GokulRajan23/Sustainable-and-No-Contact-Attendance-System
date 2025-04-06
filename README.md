# Sustainable and No Contact Attendance System

## Frameworks Used
Python, MySQL, C++, ESP32 Camera Module

## Description
A contactless attendance system that combines facial recognition with RFID-based authentication. The system is designed for hygienic and sustainable use in institutional environments, with real-time data storage and cloud-based access.

## Key Features
- Implemented facial recognition using OpenCV and Python.
- Integrated RFID verification via ESP32 and C++.
- Designed a MySQL backend to manage attendance records.
- Enabled cloud storage for remote and real-time tracking of attendance data.

## Screenshots
> (Add screenshots of the working system or UI here, for example: setup, ESP32 module, database view, etc.)

## Folder Structure
```
├── face_recognition/         # Python scripts for facial detection
├── rfid_module/              # C++ code for ESP32 RFID functionality
├── backend/                  # MySQL database scripts
├── cloud_storage/            # Scripts/config for cloud sync
├── images/                   # Screenshots and demo images
├── requirements.txt          # Python dependencies
└── README.md                 # Project readme file
```

## How to Run

### 1. Set up MySQL database
- Create a database and import the `attendance_db.sql` file.

### 2. Install Python requirements
```bash
pip install -r requirements.txt
```

### 3. Run facial recognition script
```bash
python face_recognition/face_detect.py
```

### 4. Upload code to ESP32
- Use Arduino IDE to upload `rfid_reader.ino` to the ESP32 camera module.

### 5. Start cloud sync (Optional)
```bash
python cloud_storage/sync_to_cloud.py
```

## Notes
- The ESP32 camera module is used for real-time facial capture.
- Cloud service used: *(mention Firebase / Google Sheets / AWS etc.)*
- This project was part of an initiative to design hygienic, non-contact solutions for educational institutions.

## Author
Gokul
