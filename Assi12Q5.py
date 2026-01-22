# Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output : 5 4 3 2 1 

num = int(input("Enter a number: "))

if num <= 0:
    print("Invalid input")
else:
    for i in range(num, 0, -1):
        print(i, end=" ")

# Output is:
# Enter a number: 5
# 5 4 3 2 1