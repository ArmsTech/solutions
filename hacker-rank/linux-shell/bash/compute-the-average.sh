#!/bin/bash
#
# Compute the Average Challenge

read numbers
sum=0

for (( index=0; index < "${numbers}"; index++ )); do
  read number
  sum=$((sum + number))
done

printf "%.3f" $(echo "scale = 4; ${sum} / ${numbers}" | bc)
