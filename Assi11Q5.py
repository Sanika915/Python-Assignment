# Write a program which accepts one number and checks whether it is palindrome or not.
# Input : 121
# Output : Palindrome

num = int(input("Enter a number: "))

if num < 0:
    print("Not Palindrome")
else:
    original = num
    reverse_num = 0

    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10

    if original == reverse_num:
        print("Palindrome")
    else:
        print("Not Palindrome")

# Output is:
# Enter a number: 121
# Palindrome        