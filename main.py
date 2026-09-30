students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    m1 = int(input("Enter Maths marks: "))
    m2 = int(input("Enter Python marks: "))
    m3 = int(input("Enter English marks: "))

    student = {
        "name": name,
        "roll": roll,
        "maths": m1,
        "python": m2,
        "english": m3
    }

    students.append(student)

    print("Student added successfully!")


def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for s in students:
            print("\n--------------------")
            print("Name:", s["name"])
            print("Roll Number:", s["roll"])
            print("Maths:", s["maths"])
            print("Python:", s["python"])
            print("English:", s["english"])


def search_student():
    roll = input("Enter roll number to search: ")

    found = False

    for s in students:
        if s["roll"] == roll:
            print("Student Found!")
            print("Name:", s["name"])
            print("Roll Number:", s["roll"])
            found = True

    if found == False:
        print("Student not found.")


def calculate_result():
    roll = input("Enter roll number: ")

    for s in students:
        if s["roll"] == roll:

            total = s["maths"] + s["python"] + s["english"]
            average = total / 3

            print("Student Name:", s["name"])
            print("Total Marks:", total)
            print("Average:", average)

            if s["maths"] < 40 or s["python"] < 40 or s["english"] < 40:
                print("Result: Fail")

            elif average >= 90:
                print("Grade: A")

            elif average >= 75:
                print("Grade: B")

            elif average >= 60:
                print("Grade: C")

            else:
                print("Grade: D")

            return

    print("Student not found.")


def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Calculate Result")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_result()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice. Please try again.")