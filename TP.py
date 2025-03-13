from dev_A_tools import greet
# Step 1: Basic output
print("Welcome to the Git exercise!")
print(greet("Dev.A"))

# Step 2: A simple calculation
def subtract(a, b):
     return a - b
print("5 - 2 =", subtract(5, 2))

from dev_B_tools import greet
print("Square of 4:", square(4))
# Pb: Cannot import name 'greet' from dev_B_tools

# Step 3: Random fun
import random
print("Lucky number:", random.randint(1, 100))

# Step 4: Final message
print("Congratulations!")

# Step 5: Multiplication
# def multiply(a, b):
#     return a * b
# print("3 * 4 =", multiply(3, 4))

# Step 6: User input
# name = input("Enter your name: ")
# print("Hello,", name)

# Step 7: List processing
# numbers = [1, 2, 3, 4, 5]
# print("Sum of list:", sum(numbers))