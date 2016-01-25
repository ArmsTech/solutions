# Namedtuple Challenge
"""
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks,
class and name. Your task is to help Dr. Wesley calculate the average marks of
the students.

Average=Sum of all marksTotal Students

Note:
    1. Columns can be in any order. IDs, marks, class and name can be written
       in any order in the spreadsheet.
    2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type
       of these names won't change.)
"""

from collections import namedtuple

number_of_students = int(raw_input())
student = namedtuple('student', raw_input().split())

students = [student(*raw_input().split()) for _ in range(number_of_students)]
print '{0:.2f}'.format(
    sum([float(student.MARKS) for student in students]) / number_of_students)
