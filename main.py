# Author: Patrick Nogaj
# Date: March 14th, 2020
# Submission: Programming assignment for Kargo SE Internship
# Python version: 2.7

# Utilizing sys to grab arguments from CL.
import sys

# Creating an empty dictionary titled 'firstWord'
firstWord = {}

# This is storing the value of each letter in firstWord (first argument)
# to a value, by default it will be 1 unless it already exists
# which will then update the value by 1.
for letter in str(sys.argv[1]):
    if(firstWord.get(letter)):
        firstWord[letter] = firstWord.get(letter) + 1
    else:
        firstWord[letter] = 1


