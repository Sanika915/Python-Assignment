# Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output : 6

num = int(input("Enter a number: "))
num = abs(num)

sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num //= 10

print("Sum of digits:", sum_digits)

# Output is:
# Enter a number: 123
# Sum of digits: 6