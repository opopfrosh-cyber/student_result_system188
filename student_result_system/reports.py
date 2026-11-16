from results import calculate_result


def display_report_card(student):
    total, average, grade = calculate_result(student.scores)
    print("\n========== STUDENT REPORT CARD ==========")
    print("ID:", student.student_id)
    print("Name:", student.full_name)
    print("Class:", student.class_form)
    print("Gender:", student.gender)
    print("Date of birth:", student.date_of_birth)
    print("-----------------------------------------")
    for subject, score in student.scores.items():
        print(f"{subject}: {score}")
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("Result entered:", student.result_date or "Not recorded")
    print("=========================================")


def ranked_students(students):
    return sorted(students, key=lambda s: calculate_result(s.scores)[1], reverse=True)


def class_report(students):
    if not students:
        print("No students registered.")
        return
    averages = []
    for position, student in enumerate(ranked_students(students), 1):
        total, average, grade = calculate_result(student.scores)
        print(f"{position}. {student.full_name} | Total: {total} | Average: {average:.2f} | Grade: {grade}")
        if student.scores:
            averages.append(average)
    if averages:
        print("Highest average:", max(averages))
        print("Lowest average:", min(averages))
        print("Class average:", round(sum(averages) / len(averages), 2))


def save_class_report(students, filename):
    lines = ["STUDENT RESULT MANAGEMENT SYSTEM - CLASS REPORT"]
    for position, student in enumerate(ranked_students(students), 1):
        total, average, grade = calculate_result(student.scores)
        lines.append(f"{position}. {student.full_name} | Total: {total} | Average: {average:.2f} | Grade: {grade}")
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
