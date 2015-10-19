#!/bin/bash
#
# Paste #3 Challenge

# Given a CSV file where each row contains the name of a city and its state
# separated by a comma, your task is to replace the newlines in the file with
# tabs as demonstrated in the sample.

paste -d$'\t' -s -
