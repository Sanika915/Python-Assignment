# Write a program which accepts one number and prints reverse of that number.
# Input : 123
# Output : 321

num = int(input("Enter a number: "))

sign = -1 if num < 0 else 1
num = abs(num)

reverse_num = 0

while num > 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num //= 10

reverse_num *= sign

print("Reversed number:", reverse_num)

# Output is:
# Enter a number: 123
# Reversed number: 321