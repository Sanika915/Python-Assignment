# Write a program which accepts one number and prints all even numbers till that numbers.
# Input : 10
# Output : 2 4 6 8 10

def PrintEvenNumbers(n):
    for i in range(2, n + 1, 2):
        print(i, end=" ")

n = int(input())

PrintEvenNumbers(n)

# Output is:
# Enter number :10
# 2 4 6 8 10