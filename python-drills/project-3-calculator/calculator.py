# Project 3 — Simple Calculator
# Drills: functions with arguments + return values, float input, input validation.
num1 = float(input("Enter first number: "))    # float allows decimals
num2 = float(input("Enter second number: "))
op = input("Choose operation (+, -, *, /): ")

# 1) All functions defined together at the top
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:                                 # == asks a question (not =)
        return "Error: cannot divide by zero!"
    return a / b


if op == "+":
    print("Result:", add(num1, num2))
elif op == "-":
    print("Result:", subtract(num1, num2))
elif op == "*":
    print("Result:", multiply(num1, num2))
elif op == "/":
    print("Result:", divide(num1, num2))
else:
    print("Unknown operation!")
