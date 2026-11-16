import json
import os
from student import Student


def load_students(filename):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            records = json.load(file)
        return [Student.from_dict(record) for record in records]
    except (json.JSONDecodeError, OSError, KeyError, TypeError) as error:
        print("Could not load records:", error)
        return []


def save_students(students, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump([s.to_dict() for s in students], file, indent=4)
