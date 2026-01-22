# Write a program which accepts one number and prints count of digits in that number.
# Input : 7521
# Output : 4

num = int(input("Enter a number: "))

num = abs(num)

if num == 0:
    count = 1
else:
    count = 0
    while num > 0:
        count += 1
        num //= 10

print("Count of digits:", count)

# Output is:
# Enter a number: 7521
# Count of digits: 4