#!/usr/bin/python3
"""
Simple Calculator Program

This script provides a basic text-based calculator that performs addition, subtraction, multiplication and division based on user input.

Author: Udeme Harrison
"""

# Function to add two numbers
def add(x, y):
    return x + y

# Function to substract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        print("Cannot divide by 0")
    return x / y

while True:
    # Display the menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply'for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    # Take user input
    user_input = input(": ")

    # Check the user's choicw
    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ", divide(num1, num2))
    else:
        print("Invalid input. Please enter a valid operation.")
