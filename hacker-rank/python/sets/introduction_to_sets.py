# Introduction To Sets Challenge
"""
Now, lets use our knowledge of Sets and help 'Mickey'.

Ms. Gabriel Williams is a botany professor at District College. One day, she
asked her student 'Mickey' to compute an average of all the plants with
distinct heights in her greenhouse.
"""

raw_input()
distinct_heights = set(map(int, raw_input().split()))

print sum(distinct_heights) / float(len(distinct_heights))
