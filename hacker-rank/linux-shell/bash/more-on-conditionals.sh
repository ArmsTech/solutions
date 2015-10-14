#!/bin/bash
#
# More On Conditionals Challenge

read x
read y
read z

if (( "${x}" == "${y}" && "${x}" == "${z}" )); then
  echo "EQUILATERAL"
elif (( "${x}" == "${y}" || "${y}" == "${z}" || "${x}" == "${z}" )); then
  echo "ISOSCELES"
else
  echo "SCALENE"
fi
