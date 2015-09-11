# Nested List Challenge
"""
There is a classroom of 'n' students and you are given their names and marks
in physics. Store them in a nested list and print the name of each student
who got the second lowest marks in physics.
NOTE: If there are more than one student getting same marks, make sure you
print the names of all students in alphabetical order, in different lines.
"""

students = []
students_count = int(raw_input())

for _ in range(students_count):
    students.append([raw_input(), float(raw_input())])

grades = set([student[1] for student in students])
second_lowest_grade = sorted(list(grades)).pop(1)

names = [name for name, grade in students if grade == second_lowest_grade]
for name in sorted(names):
    print name
