# Student-planner
Student Management System

A simple terminal-based Student Management System developed in Python.
The program allows users to add, view, search, calculate results, and delete student records.


Features


Add Student

Enter student name and roll number.
Enter marks for Maths, Python, and English.
Stores the student record in a list of dictionaries.

Display Students

Displays all stored student records.
Shows name, roll number, and marks.
Displays a message if no records exist.

Search Student

Searches for a student using their roll number.
Displays the student's name and roll number if found.

Calculate Result

Calculates total and average marks.
Checks whether the student has passed all subjects.
Assigns a grade based on the average.
A student scoring below 40 in any subject receives a Fail result.

Delete Student

Deletes a student using their roll number.

Exit

Terminates the program.


Technologies Used


Python 3

Lists

Dictionaries

Functions

Loops

Conditional statements

User input

Basic arithmetic operations


Data Structure

Student records are stored in a list called students.


Each student is represented using a dictionary:


{
    "name": "Rahul",
    "roll": "101",
    "maths": 85,
    "python": 92,
    "english": 78
}

Program Structure

Function	Purpose
add_student()	Adds a new student record
display_students()	Displays all student records
search_student()	Searches for a student by roll number
calculate_result()	Calculates total, average, and grade
delete_student()	Removes a student record
Main Menu	Provides options and controls program execution

Grading System

Average Marks	Grade
90 and above	A
75–89	B
60–74	C
Below 60	D

Passing condition: A student must score at least 40 marks in every subject.


If the student scores below 40 in any subject, the result is Fail, regardless of their average.


How to Run

1. Install Python

Check that Python 3 is installed:


python --version

2. Run the program

Save the Python code as:


student_management.py

Then run:


python student_management.py

Example Menu

===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Display Students
3. Search Student
4. Calculate Result
5. Delete Student
6. Exit

Enter your choice:

Example Result

Enter roll number: 101

Student Name: Rahul
Total Marks: 255
Average: 85.0
Grade: B

Limitations


Student records are stored only while the program is running.

Closing the program removes all stored records.

Marks must be entered as integers.

There is currently no duplicate roll-number validation.

The program runs entirely in the terminal.


Future Improvements


Save records permanently using CSV or JSON.

Add input validation for marks.

Prevent duplicate roll numbers.

Add student update/edit functionality.

Add more subjects.

Generate a complete marksheet.

Add sorting by marks, name, or roll number.

Add a class topper/merit-list feature.


Author

Student Management System — Python Project


Built as a beginner-friendly Python project demonstrating the use of functions, lists, dictionaries, loops, conditional statements, and user input.

