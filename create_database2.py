import sqlite3
import os

# Check if the file exists
if os.path.exists('example.db'):
    # Delete the file
    os.remove('example.db')
    print("File 'example.db' deleted successfully.")
else:
    print("File 'example.db' does not exist.")

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        major TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        credits INTEGER
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Enrollments (
        student_id INTEGER,
        course_id INTEGER,
        grade TEXT,
        FOREIGN KEY (student_id) REFERENCES Students (id),
        FOREIGN KEY (course_id) REFERENCES Courses (id)
    )
''')

# Insert data into the tables
cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Andi', 21, 'Computer Science')")
cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Bella', 22, 'Mathematics')")
cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Chika', 23, 'Physics')")
cursor.execute("INSERT INTO Students (name, age, major) VALUES ('David', 20, 'Chemistry')")
cursor.execute("INSERT INTO Students (name, age, major) VALUES ('Evan', 22, 'Biology')")

cursor.execute("INSERT INTO Courses (name, credits) VALUES ('Calculus', 3)")
cursor.execute("INSERT INTO Courses (name, credits) VALUES ('Physics', 4)")
cursor.execute("INSERT INTO Courses (name, credits) VALUES ('Chemistry', 4)")
cursor.execute("INSERT INTO Courses (name, credits) VALUES ('Biology', 3)")
cursor.execute("INSERT INTO Courses (name, credits) VALUES ('Computer Science', 3)")

cursor.execute("INSERT INTO Enrollments (student_id, course_id, grade) VALUES (1, 5, 'A')")
cursor.execute("INSERT INTO Enrollments (student_id, course_id, grade) VALUES (2, 1, 'B')")
cursor.execute("INSERT INTO Enrollments (student_id, course_id, grade) VALUES (3, 2, 'A')")
cursor.execute("INSERT INTO Enrollments (student_id, course_id, grade) VALUES (4, 3, 'B')")
cursor.execute("INSERT INTO Enrollments (student_id, course_id, grade) VALUES (5, 4, 'A')")

# Commit the changes
conn.commit()

# Read data from the tables
cursor.execute("SELECT * FROM Students")
students = cursor.fetchall()
print("Students:")
for student in students:
    print(student)

cursor.execute("SELECT * FROM Courses")
courses = cursor.fetchall()
print("\nCourses:")
for course in courses:
    print(course)

cursor.execute("SELECT * FROM Enrollments")
enrollments = cursor.fetchall()
print("\nEnrollments:")
for enrollment in enrollments:
    print(enrollment)

# Close the connection
conn.close()
