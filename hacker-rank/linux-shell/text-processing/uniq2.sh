#!/bin/bash
#
# Uniq #2 Challenge

# Given a text file, count the number of times each line repeats itself (only
# consider consecutive repetitions).

uniq -c - |tr -s [:space:] |cut -d' ' -f2-
