# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.
# Input : 10 20
# Output : 20 is greater

def ChkGreater(num1, num2):
    if num1 > num2:
        print(num1, "is greater")
    else:
        print(num2, "is greater")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

ChkGreater(a, b)

# Output is
# Enter first number: 10
# Enter second number: 20
# 20 is greater