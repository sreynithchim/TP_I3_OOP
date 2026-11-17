import json
"""I decided to choose JSON File """
class Student:
    """Structure (Class): Defines one student record"""
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

"""Array (List): Stores many student records"""
students = []


def add_student():
    """Add Student"""
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))

    student = Student(student_id, name, age)
    students.append(student)
    print("Student added successfully!")



def search_student():
    """Search for a student"""
    student_id = input("Enter Student ID to search: ")

    for student in students:
        if student.student_id == student_id:
            print("ID:", student.student_id)
            print("Name:", student.name)
            print("Age:", student.age)
            return

    print("Student not found!")



def edit_student():
    """Edit student information"""
    student_id = input("Enter Student ID to edit: ")

    for student in students:
        if student.student_id == student_id:
            student.name = input("Enter new name: ")
            student.age = int(input("Enter new age: "))
            print("Student updated successfully!")
            return

    print("Student not found!")



def delete_student():
    """Delete a Student"""
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found!")


def display_students():
    """Display all Students"""
    if not students:
        print("No student records found!")
        return

    for student in students:
        print("ID:", student.student_id)
        print("Name:", student.name)
        print("Age:", student.age)
        print("-------------------")




def save_file():
    """4. File: Save student records"""
    data = []

    for student in students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age
        })

    with open("students.json", "w") as file:
        json.dump(data, file)

    print("Data saved successfully!")


def load_file():
    """Load File"""
    try:
        with open("students.json", "r") as file:
            data = json.load(file)
        students.clear()
        for item in data:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"]
            )
            students.append(student)

        print("Data loaded successfully!")

    except FileNotFoundError:
        print("No saved file found!")


load_file()
"""Main Function"""
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Edit Student")
    print("4. Delete Student")
    print("5. Display Students")
    print("6. Save Data")
    print("7. Exit")

    choice = input("Choose an option : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        search_student()

    elif choice == "3":
        edit_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        display_students()

    elif choice == "6":
        save_file()

    elif choice == "7":
        save_file()
        print("Thank you.")
        break

    else:
        print("Invalid.Try agian my cuties")