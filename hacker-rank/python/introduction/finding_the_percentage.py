# Finding The Percentage Challenge
"""
There is a record of 'n' students, each record having name of student,
percent marks obtained in Maths, Physics and Chemistry. Marks can be floating
values. The user enters an integer 'n' followed by names and marks for the
'n' students. You are required to save the record in a dictionary data type.
The user then enters name of a student and you are required to print the
average percentage marks obtained by that student, correct to two decimal
places.
"""

records = {}
n = int(raw_input())

for _ in range(0, n):
    record = raw_input()
    name, math, physics, chemistry = record.split()
    records[name] = [float(math), float(physics), float(chemistry)]

student = raw_input()
print '%.2f' % (sum(records[student]) / len(records[student]))
