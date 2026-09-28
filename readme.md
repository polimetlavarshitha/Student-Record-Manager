# Student Record Manager

A simple **Python-based Student Record Manager** developed as a Module 2 assignment.

The application allows users to add student records, view saved records, validate email addresses, and store data locally using a JSON file.

## Features

* Interactive command-line menu
* Add student records
* View all student records
* Email validation using Python Regex
* Age validation
* Save records to `students.json`
* Automatically load existing records when the program starts
* Exception handling for invalid inputs
* Handles missing or invalid JSON files
* Handles file permission and file operation errors
* Beginner-friendly Python implementation

## Technologies Used

* **Python 3**
* `json` — for storing and reading student records
* `re` — for email validation using Regular Expressions
* `os` — for checking file availability

## Project Structure

```text
Student-Record-Manager/
│
├── student_manager.py
├── students.json
└── README.md
```

> `students.json` will be created automatically when the first student is added.

## How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installation using:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the Project Folder

```bash
cd Student-Record-Manager
```

### 4. Run the Program

```bash
python student_manager.py
```

## How It Works

When the program starts, it displays an interactive menu:

```text
==============================
     STUDENT RECORD MANAGER
==============================
1. Add Student
2. View All Students
3. Exit
==============================
```

### Add Student

Select option `1` and enter:

* Student name
* Student email
* Student age

Example:

```text
Enter student name: Rahul
Enter student email: rahul@gmail.com
Enter student age: 20
Student added successfully!
```

The information is then stored in `students.json`.

### View Students

Select option `2` to display all saved records.

Example:

```text
--- Student Records ---

Student 1
Name  : Rahul
Email : rahul@gmail.com
Age   : 20
```

### Exit

Select option `3` to safely exit the application.

## Email Validation

The project uses Python's `re` library to check whether the entered email follows a basic valid email pattern.

For example:

```text
rahul@gmail.com
```

is accepted, while:

```text
rahul@gmail
```

is rejected.

## Exception Handling

The application includes error handling for common problems such as:

* Invalid age input
* Empty student name
* Invalid email format
* Missing `students.json`
* Invalid JSON data
* File permission errors
* Other file operation errors
* Keyboard interruption
* Invalid menu choices

Example:

```text
Enter student age: abc
Error: Age must be a valid number between 1 and 120.
```

## Data Storage

Student records are stored locally in a JSON file called:

```text
students.json
```

Example:

```json
[
    {
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "age": 20
    }
]
```

The file is automatically loaded when the application starts and updated whenever a new student is added.

## Learning Objectives

This project demonstrates the following Python concepts:

* Variables and data types
* Functions
* Lists and dictionaries
* Loops
* Conditional statements
* File handling
* JSON data storage
* Regular expressions
* Exception handling
* User input validation
* Modular program structure

## Future Improvements

Possible improvements for future versions include:

* Search for a student
* Update student information
* Delete student records
* Student ID generation
* Sorting student records
* Export records to CSV
* Graphical user interface
* Database integration using SQLite

## Author

**Your Name**

B.Tech Computer Science and Engineering Student

## License

This project is created for educational purposes.
## Sample Output

### Adding a Student

```text
Enter your choice (1-3): 1

Enter student name: Rahul
Enter student email: rahul@gmail.com
Enter student age: 20

Student added successfully!
Enter your choice (1-3): 2

--- Student Records ---

Student 1
Name  : Rahul
Email : rahul@gmail.com
Age   : 20
Enter your choice (1-3): 1

Enter student name: Rahul
Enter student email: rahul@gmail

Error: Invalid email format.
Enter your choice (1-3): 1

Enter student name: Rahul
Enter student email: rahul@gmail.com
Enter student age: abc

Error: Age must be a valid number between 1 and 120.
Enter your choice (1-3): 5

Error: Please enter a valid option (1, 2, or 3).
