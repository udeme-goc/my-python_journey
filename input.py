#!/usr/bin/python3

"""
This function is a test for how user input works in a python script.
"""

# Prompt the user for an integer
user_input = input("Enter a number: ")

# Convert the user's input to an inter
try:
    user_float = float(user_input)
    print("You entered the number: ", user_float)
except ValueError:
    print("Invalid input. Please enter a number.")
