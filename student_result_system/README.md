# New Horizon Student Result Management System

A menu-driven Python program for student registration, score recording, grading, report cards, class ranking and JSON data storage.

## Run the project
1. Install Python 3.8 or newer.
2. Open a terminal in this folder.
3. Run `python main.py` (or `python3 main.py`).
4. Follow the numbered menu.

No third-party packages are required. The `data/students.json` file is created automatically when records are saved.

## Files
- `main.py`: menu and program flow
- `student.py`: Student class and conversion to/from dictionaries
- `results.py`: total, average and grade calculations
- `storage.py`: JSON loading and saving
- `reports.py`: report cards, class ranking and class report

## Grade scale in this version
A = 70–100; B = 60–69; C = 50–59; D = 45–49; F = below 45.

Confirm the grading scale with your lecturer. Test the system, understand the code, and personalise it before submitting your individual assignment.
