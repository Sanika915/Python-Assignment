# Write a program which accepts one nuber and prints multiplication table of that number.
# Input : 4
# Output: 4 8 12 16 20 24 28 32 36 40 

def PrintMultiplicationTable(num):
    for i in range(1, 11):
        print(num * i, end=" ")

num = int(input())

PrintMultiplicationTable(num)

# Output is:
# Enter a number : 4
# 4 8 12 16 20 24 28 32 36 40