def calculate_result(scores):
    if not scores:
        return 0, 0.0, "N/A"
    total = sum(scores.values())
    average = total / len(scores)
    if average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 45:
        grade = "D"
    else:
        grade = "F"
    return total, average, grade
