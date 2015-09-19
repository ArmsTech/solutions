# Zipped Challenge
"""
The National University, conducts an examination of N students in X subjects.
Your task is to compute average scores of each student.
"""

grades = []
_, students = raw_input().split()

for _ in range(int(students)):
    grades.append(map(float, raw_input().split()))

for student_grades in zip(*grades):
    print sum(student_grades) / len(student_grades)
