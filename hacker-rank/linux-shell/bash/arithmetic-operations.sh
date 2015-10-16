#!/bin/bash
#
# Arithmetic Operations Challenge

read expression

printf "%.3f" $(echo "scale = 4; ${expression}" | bc)
