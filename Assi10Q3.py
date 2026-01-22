# Write a program which accepts one number and prints factorial of that number.
# Input: 5
# Output: 120

def Factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input())

result = Factorial(n)
print(result)

# Output is
# Enter number: 5
# Sum : 120