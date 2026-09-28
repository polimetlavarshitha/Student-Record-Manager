import json
import os
import re

FILE_NAME = "students.json"


def validate_email(email):
    """Validate email format using regular expression."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def load_students():
    """Load student records from students.json."""
    try:
        if not os.path.exists(FILE_NAME):
            return []

        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: Invalid data format in students.json.")
            return []

        return data

    except json.JSONDecodeError:
        print("Error: students.json contains invalid JSON data.")
        return []

    except PermissionError:
        print("Error: Permission denied while reading the file.")
        return []

    except OSError as e:
        print(f"Error while loading students: {e}")
        return []


def save_students(students):
    """Save student records to students.json."""
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(students, file, indent=4)

    except PermissionError:
        print("Error: Permission denied while saving the file.")

    except OSError as e:
        print(f"Error while saving students: {e}")


def add_student(students):
    """Add a new student record."""

    print("\n--- Add Student ---")

    try:
        name = input("Enter student name: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        email = input("Enter student email: ").strip()

        if not validate_email(email):
            raise ValueError("Invalid email format.")

        age_input = input("Enter student age: ").strip()

        try:
            age = int(age_input)

            if age <= 0 or age > 120:
                raise ValueError("Age must be between 1 and 120.")

        except ValueError:
            print("Error: Age must be a valid number between 1 and 120.")
            return

        student = {
            "name": name,
            "email": email,
            "age": age
        }

        students.append(student)
        save_students(students)

        print("Student added successfully!")

    except ValueError as e:
        print(f"Error: {e}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")


def view_students(students):
    """Display all student records."""

    print("\n--- Student Records ---")

    if not students:
        print("No student records found.")
        return

    for index, student in enumerate(students, start=1):
        print(f"\nStudent {index}")
        print(f"Name  : {student.get('name', 'N/A')}")
        print(f"Email : {student.get('email', 'N/A')}")
        print(f"Age   : {student.get('age', 'N/A')}")


def display_menu():
    """Display the main menu."""

    print("\n==============================")
    print("     STUDENT RECORD MANAGER")
    print("==============================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Exit")
    print("==============================")


def main():
    """Main program loop."""

    students = load_students()

    print("Welcome to Student Record Manager!")

    while True:
        try:
            display_menu()

            choice = input("Enter your choice (1-3): ").strip()

            if choice == "1":
                add_student(students)

            elif choice == "2":
                view_students(students)

            elif choice == "3":
                print("Thank you for using Student Record Manager!")
                print("Goodbye!")
                break

            else:
                print("Error: Please enter a valid option (1, 2, or 3).")

        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print("Goodbye!")
            break

        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()