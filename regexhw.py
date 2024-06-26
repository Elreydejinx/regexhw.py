# 1. Python Regular Expressions Mastery

# Task 1: Name Verification

# Problem Statement: 
#  Write a function that takes in a list of names,
#  and verifies that the names are valid names using a regex pattern and match(),
#  and prints the name if it is valid, 
#  "Invalid name" if the name is not.

#  Use the following list as an argument to test your function.



# Code Example:
import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna ", "programming is cool"]

def filter_names(names):
    pattern = re.compile(r"([A-Z][a-z]+) ([A-Z][a-z]*)?\s?([A-Z][a-z]+)")
    for name in names:
        if re.match(pattern, name):
            print(name)
        else:
            print("Invalid name")
    

filter_names(names)


