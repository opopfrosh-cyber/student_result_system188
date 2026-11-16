from datetime import datetime
from student import Student
from storage import load_students, save_students
from results import calculate_result
from reports import display_report_card, class_report, save_class_report

DATA_FILE = "data/students.json"
SUBJECTS = ["English", "Mathematics", "Biology", "Chemistry", "Physics"]


def find_student(students, student_id):
    for student in students:
        if student.student_id.lower() == student_id.lower():
            return student
    return None


def add_student(students):
    student_id = input("Student ID: ").strip()
    if not student_id or find_student(students, student_id):
        print("Invalid or duplicate student ID.")
        return
    name = input("Full name: ").strip()
    class_form = input("Class/Form: ").strip()
    gender = input("Gender: ").strip()
    dob = input("Date of birth (DD/MM/YYYY): ").strip()
    if not all([name, class_form, gender, dob]):
        print("All fields are required.")
        return
    students.append(Student(student_id, name, class_form, gender, dob))
    save_students(students, DATA_FILE)
    print("Student registered successfully.")


def view_students(students):
    if not students:
        print("No students registered.")
    for s in students:
        print(f"{s.student_id} | {s.full_name} | {s.class_form}")


def search_student(students):
    term = input("Enter student ID or name: ").strip().lower()
    found = [s for s in students if term in s.student_id.lower() or term in s.full_name.lower()]
    if not found:
        print("No matching student found.")
    for s in found:
        print(f"{s.student_id} | {s.full_name} | {s.class_form}")


def update_student(students):
    s = find_student(students, input("Student ID to update: ").strip())
    if not s:
        print("Student not found.")
        return
    print("Press Enter to keep the current value.")
    s.full_name = input(f"Full name [{s.full_name}]: ").strip() or s.full_name
    s.class_form = input(f"Class/Form [{s.class_form}]: ").strip() or s.class_form
    s.gender = input(f"Gender [{s.gender}]: ").strip() or s.gender
    s.date_of_birth = input(f"Date of birth [{s.date_of_birth}]: ").strip() or s.date_of_birth
    save_students(students, DATA_FILE)
    print("Student details updated.")


def delete_student(students):
    s = find_student(students, input("Student ID to delete: ").strip())
    if not s:
        print("Student not found.")
        return
    if input(f"Delete {s.full_name}? (y/n): ").lower() == "y":
        students.remove(s)
        save_students(students, DATA_FILE)
        print("Student deleted.")


def record_scores(students):
    s = find_student(students, input("Student ID: ").strip())
    if not s:
        print("Student not found.")
        return
    scores = {}
    for subject in SUBJECTS:
        while True:
            try:
                score = float(input(f"{subject} score (0-100): "))
                if 0 <= score <= 100:
                    scores[subject] = score
                    break
                print("Score must be between 0 and 100.")
            except ValueError:
                print("Enter a valid number.")
    s.scores = scores
    s.result_date = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_students(students, DATA_FILE)
    print("Scores saved.")


def main():
    students = load_students(DATA_FILE)
    while True:
        print("\n===== NEW HORIZON STUDENT RESULT SYSTEM =====")
        print("1. Register student\n2. View all students\n3. Search student")
        print("4. Update student\n5. Delete student\n6. Record/update scores")
        print("7. Individual report card\n8. Class results/statistics")
        print("9. Save class report to text file\n0. Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                update_student(students)
            elif choice == "5":
                delete_student(students)
            elif choice == "6":
                record_scores(students)
            elif choice == "7":
                s = find_student(students, input("Student ID: ").strip())
                display_report_card(s) if s else print("Student not found.")
            elif choice == "8":
                class_report(students)
            elif choice == "9":
                save_class_report(students, "class_report.txt")
                print("Saved as class_report.txt")
            elif choice == "0":
                save_students(students, DATA_FILE)
                print("Records saved. Goodbye.")
                break
            else:
                print("Choose a valid menu number.")
        except (OSError, ValueError) as error:
            print("An error occurred:", error)


if __name__ == "__main__":
    main()
