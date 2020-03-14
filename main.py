# Author: Patrick Nogaj
# Date: March 14th, 2020
# Submission: Programming assignment for Kargo SE Internship
# Python version: 2.7

# Utilizing sys to grab arguments from CL.
import sys

# Creating an empty dictionary titled 'firstWord'
# Storing the value of first argument into a string
firstWord = {}
firstArgument = str(sys.argv[1])

# This is storing the value of each letter in firstWord (first argument)
# to a value, by default it will be 1 unless it already exists
# which will then update the value by 1.
for letter in firstArgument:
    if(firstWord.get(letter)):
        firstWord[letter] = firstWord.get(letter) + 1
    else:
        firstWord[letter] = 1

# Storing the second argument into a string
secondArgument = str(sys.argv[2])

# If the value of the dictionary equals the length of argument 2
# return true
# otherwise, they are not the same thus it is false.
if(len(firstWord) == len(secondArgument)):
   print 'true'
else:
    print 'false'

