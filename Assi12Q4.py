# Write a program which accepts one number and prints that many numbers starting from 1.
# Input : 5
# Output : 1 2 3 4 5

num = int(input("Enter a number: "))

if num <= 0:
    print("Invalid input")
else:
    for i in range(1, num + 1):
        print(i, end=" ")

# Output is:
# Enter a number: 5
# 1 2 3 4 5