"""Convert scores into grades"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    "Cashel": 101,
}


def run_student_grades():
    student_grades = {}
    count = 0
    for student, score in student_scores.items():
        if 90 < score <= 100:
            student_grades[student] = "Outstanding"
        elif 80 < score < 90:
            student_grades[student] = "Exceeds Expectations"
        elif 70 < score < 80:
            student_grades[student] = "Acceptable"
        elif score <= 70:
            student_grades[student] = "Fail"
        else:
            student_scores[student] = int((input(f"What is {[key for key in student_scores.keys()][count]}'s score?\n")))

        count += 1

    return student_grades


run_student_grades()
print(run_student_grades())


