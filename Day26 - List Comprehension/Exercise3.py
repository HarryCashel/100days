"""Dictionary Comprehension"""

# Syntax
# new_dict = {new_key: new_value for item in list}

# Conditional syntax
# new_dict = {new_key: new_value for (key, value) in dict.items() if conditional}
import random

student_names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = [90, 89, 78, 67, 75, 73]

student_scores = {name: score for (name, score) in zip(student_names, student_score)}

print(student_scores)

# Random scores

student_scores = {name: random.randint(1, 100) for name in student_names}

passed_student = {name: score for (name, score) in student_scores.items() if score > 75}

print(student_scores)
print(passed_student)

