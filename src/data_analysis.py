#!/usr/bin/env python3
"""Basic Data Analysis Script"""

import os

def load_students(filename):
    """Read the CSV file and return a list of student records."""
    students = []
    with open(filename, "r") as f:
        lines = f.readlines()[1:]  # Skip the header line
        for line in lines:
            name, age, grade, subject = line.strip().split(",")
            students.append({
                "name": name,
                "age": int(age),
                "grade": int(grade),
                "subject": subject
            })
    return students


def calculate_average_grade(students):
    """Calculate average grade of all students."""
    total = sum(s["grade"] for s in students)
    return total / len(students)


def count_math_students(students):
    """Count how many students study Math."""
    return sum(1 for s in students if s["subject"].lower() == "math")


def generate_report(total, average, math_count):
    """Create a formatted report string."""
    report = (
        f"Total students: {total}\n"
        f"Average grade: {average:.1f}\n"
        f"Number of Math students: {math_count}\n"
    )
    return report


def save_report(report, filename):
    """Write the report to output file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(report)
    print(f"✅ Report saved to {filename}")


def main():
    """Main function that orchestrates the analysis."""
    students = load_students("data/students.csv")
    total = len(students)
    average = calculate_average_grade(students)
    math_count = count_math_students(students)

    report = generate_report(total, average, math_count)
    save_report(report, "output/analysis_report.txt")


if __name__ == "__main__":
    main()
