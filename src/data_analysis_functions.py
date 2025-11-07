#!/usr/bin/env python3
"""Advanced Data Analysis Script with Modular Design"""

import os

def load_data(filename):
    """Generic loader that checks file extension."""
    if filename.endswith(".csv"):
        return load_csv(filename)
    else:
        raise ValueError("Unsupported file type! Only CSV files are allowed.")


def load_csv(filename):
    """Load CSV data and return a list of students."""
    students = []
    with open(filename, "r") as f:
        lines = f.readlines()[1:]  # skip header
        for line in lines:
            name, age, grade, subject = line.strip().split(",")
            students.append({
                "name": name,
                "age": int(age),
                "grade": int(grade),
                "subject": subject
            })
    return students


def analyze_data(students):
    """Perform analysis and return a dictionary of statistics."""
    grades = [s["grade"] for s in students]
    subjects = [s["subject"] for s in students]

    results = {
        "total_students": len(students),
        "average_grade": sum(grades) / len(grades),
        "highest_grade": max(grades),
        "lowest_grade": min(grades),
        "subject_counts": {sub: subjects.count(sub) for sub in set(subjects)},
        "grade_distribution": analyze_grade_distribution(grades)
    }
    return results


def analyze_grade_distribution(grades):
    """Count grades by letter range and percentage."""
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for g in grades:
        if g >= 90:
            distribution["A"] += 1
        elif g >= 80:
            distribution["B"] += 1
        elif g >= 70:
            distribution["C"] += 1
        elif g >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    total = len(grades)
    return {k: f"{(v / total) * 100:.1f}%" for k, v in distribution.items()}


def save_results(results, filename):
    """Save detailed analysis report to a text file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("=== Detailed Analysis Report ===\n")
        f.write(f"Total students: {results['total_students']}\n")
        f.write(f"Average grade: {results['average_grade']:.1f}\n")
        f.write(f"Highest grade: {results['highest_grade']}\n")
        f.write(f"Lowest grade: {results['lowest_grade']}\n\n")

        f.write("Subject counts:\n")
        for sub, count in results["subject_counts"].items():
            f.write(f"  {sub}: {count}\n")

        f.write("\nGrade distribution:\n")
        for grade, pct in results["grade_distribution"].items():
            f.write(f"  {grade}: {pct}\n")

    print(f"✅ Detailed report saved to {filename}")


def main():
    """Run the full advanced data analysis workflow."""
    students = load_data("data/students.csv")
    results = analyze_data(students)
    save_results(results, "output/analysis_report.txt")


if __name__ == "__main__":
    main()

