# question 1: using a for loop with a list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    #--------------------------------------------------------------
    # question 2: using a while loop for countdown
    countdown = 5
while countdown >= 1:
    print(countdown)
    countdown -= 1

#--------------------------------------------------------------
# question 3: using a for loop with range()
for i in range(1, 11):
    print(f"(1) + (i ** 2)")

    #--------------------------------------------------------------
# question 4: using the random module 
import random
colurs = ["red", "green", "blue", "yellow", "purple"]
for _ in range (3):
    print(random.choice(colurs))
 #--------------------------------------------------------------
 # question 5: creating and using a custom module 

 import math_operation

print(math_operation.add(10, 5))
print(math_operation.subtract(10, 5))
print(math_operation.multiply(10, 5))
print(math_operation.divide(10, 5))  

  # Simple calculator using a while loop
while True:
    print("\n--- Calculator ---")
    print("Operations: add, subtract, multiply, divide, quit")
    operation = input("Enter operation: ").strip().lower()

    if operation == "quit":
        print("Goodbye!")
        break

    if operation not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid operation. Try again.")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == "add":
        print(f"Result: {math_operations.add(a, b)}")
    elif operation == "subtract":
        print(f"Result: {math_operations.subtract(a, b)}")
    elif operation == "multiply":
        print(f"Result: {math_operations.multiply(a, b)}")
    elif operation == "divide":
        print(f"Result: {math_operations.divide(a, b)}")

# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"