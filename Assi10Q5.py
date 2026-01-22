# Write a program which accepts one number and prints all odd numbers ti that numbers.

def PrintOddNumbers(n):
    for i in range(1, n + 1, 2):
        print(i, end=" ")

n = int(input())

PrintOddNumbers(n)

# Output is:
# Enter a number : 10
# 1 3 5 7 9