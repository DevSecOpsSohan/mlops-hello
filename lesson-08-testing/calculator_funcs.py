# Calculator functions only (no input()) — so they can be imported and tested.
# Same logic as Project 3, just without the interactive menu.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero!"
    return a / b
