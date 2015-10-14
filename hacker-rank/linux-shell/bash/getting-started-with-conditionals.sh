#!/bin/bash
#
# Getting Started With Conditionals Challenge

read char

if [[ "${char}" == "y" || "${char}" == "Y" ]]; then
  echo "YES"
elif [[ "${char}" == "n" || "${char}" == "N" ]]; then
  echo "NO"
fi
