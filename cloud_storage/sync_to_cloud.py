import mysql.connector
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Google Sheets API setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open your Google Sheet (replace with your own title)
sheet = client.open("Attendance Cloud Backup").sheet1

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="attendance_system"
)
cursor = db.cursor()

# Fetch attendance logs
cursor.execute("""
    SELECT u.name, a.check_in_time, a.method, a.status
    FROM attendance_logs a
    JOIN users u ON a.user_id = u.user_id
""")
rows = cursor.fetchall()

# Write to Google Sheet
sheet.clear()  # Optional: clear previous data
sheet.append_row(["Name", "Check-in Time", "Method", "Status"])  # Headers

for row in rows:
    sheet.append_row([row[0], row[1].strftime("%Y-%m-%d %H:%M:%S"), row[2], row[3]])

print("✅ Attendance logs synced to Google Sheets!")

# Close DB connection
cursor.close()
db.close()
