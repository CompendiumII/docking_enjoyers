import mysql.connector
import statistics
import os
from pymongo import MongoClient

# Environment variables for MySQL connection
MYSQL_HOST = "mysql"
MYSQL_USER = "user1"
MYSQL_PASSWORD = "password1"
MYSQL_DB = "analytics_data"

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DB
)

cursor = conn.cursor()

# Execute a SQL query to fetch the student grades
cursor.execute("SELECT grade FROM student_grades")

grades = [row[0] for row in cursor.fetchall()]

# Perform analytics on the grades
min_grade = float(min(grades))
max_grade = float(max(grades))
avg_grade = float(statistics.mean(grades))

print(f"Minimum Grade: {min_grade}")
print(f"Maximum Grade: {max_grade}")
print(f"Average Grade: {avg_grade}")

mongo_client = MongoClient("mongodb://admin:adminpassword@mongo_service:27017/")
db = mongo_client["assignment_1"]
collection = db["student_grades"]
collection.drop()
collection = db["student_grades"]
collection.insert_one({"Minimum Grade": min_grade})
collection.insert_one({"Maximum Grade": max_grade})
collection.insert_one({"Average Grade": avg_grade})

new = collection.find()
for item in new:
    print(item)
mongo_client.close()
cursor.close()
conn.close()