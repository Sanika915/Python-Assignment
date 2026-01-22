# Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Not possible (division by zero)")

# Output is:
# Enter first number: 93
# Enter second number: 5
# Addition: 98.0
# Subtraction: 88.0
# Multiplication: 465.0
# Division: 18.6