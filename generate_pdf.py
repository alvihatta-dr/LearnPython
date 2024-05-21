import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Read data from the tables
c.execute('SELECT * FROM Students')
students_data = c.fetchall()

c.execute('SELECT * FROM Courses')
courses_data = c.fetchall()

c.execute('SELECT * FROM Enrollments')
enrollments_data = c.fetchall()

conn.close()

# Prepare PDF
pdf_path = "database_example(3).pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
elements = []

# Title
styles = getSampleStyleSheet()
title = Paragraph("Database: Example", styles['Title'])
elements.append(title)

# Function to create a table with data
def create_table(data, col_names):
    table_data = [col_names] + data
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    return table

# Students Table
elements.append(Paragraph("Table: Students", styles['Heading2']))
students_table = create_table(students_data, ["ID", "Name", "Age", "Major"])
elements.append(students_table)

# Courses Table
elements.append(Paragraph("Table: Courses", styles['Heading2']))
courses_table = create_table(courses_data, ["CourseID", "CourseName", "Credits"])
elements.append(courses_table)

# Enrollments Table
elements.append(Paragraph("Table: Enrollments", styles['Heading2']))
enrollments_table = create_table(enrollments_data, ["EnrollmentID", "StudentID", "CourseID"])
elements.append(enrollments_table)

# Build PDF
doc.build(elements)

print(f"PDF generated and saved to {pdf_path}")
