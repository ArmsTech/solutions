#!/bin/bash
#
# Filter An Array With Patterns Challenge

# Given a list of countries, each on a new line, your task is to read them
# into an array and then filter out (remove) all the names containing the
# letter 'a' or 'A' in them.

countries=($(cat))
echo ${countries[@]/*[A|a]*/}
