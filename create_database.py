import sqlite3

# Create SQLite database and connect
conn = sqlite3.connect('example(1).db')
c = conn.cursor()

# Drop tables if they exist
c.execute('''DROP TABLE IF EXISTS Students''')
c.execute('''DROP TABLE IF EXISTS Courses''')
c.execute('''DROP TABLE IF EXISTS Enrollments''')

# Create tables
c.execute('''CREATE TABLE Students (
                ID INTEGER PRIMARY KEY,
                Name TEXT,
                Age INTEGER,
                Major TEXT)''')

c.execute('''CREATE TABLE Courses (
                CourseID INTEGER PRIMARY KEY,
                CourseName TEXT,
                Credits INTEGER)''')

c.execute('''CREATE TABLE Enrollments (
                EnrollmentID INTEGER PRIMARY KEY,
                StudentID INTEGER,
                CourseID INTEGER,
                FOREIGN KEY (StudentID) REFERENCES Students (ID),
                FOREIGN KEY (CourseID) REFERENCES Courses (CourseID))''')

# Insert data into tables
students = [
    (1, 'Adinda', 20, 'Computer Science'),
    (2, 'Bella', 22, 'Mathematics'),
    (3, 'Chika', 23, 'Physics'),
    (4, 'David', 21, 'Biology'),
    (5, 'Evan', 20, 'Chemistry')
]
courses = [
    (101, 'Calculus', 4),
    (102, 'Physics', 3),
    (103, 'Biology', 4),
    (104, 'Chemistry', 3),
    (105, 'Computer Science', 4)
]
enrollments = [
    (1, 1, 101),
    (2, 2, 102),
    (3, 3, 103),
    (4, 4, 104),
    (5, 5, 105)
]

c.executemany('INSERT INTO Students VALUES (?, ?, ?, ?)', students)
c.executemany('INSERT INTO Courses VALUES (?, ?, ?)', courses)
c.executemany('INSERT INTO Enrollments VALUES (?, ?, ?)', enrollments)

# Commit the changes and close the connection
conn.commit()
conn.close()
