# Write a program which accepts one number and prints binary equivalent.

num = int(input("Enter a number: "))

if num < 0:
    print("Negative numbers not handled in this version")
else:
    if num == 0:
        print("Binary: 0")
    else:
        binary = ""
        n = num
        while n > 0:
            binary = str(n % 2) + binary
            n //= 2
        print("Binary:", binary)

# Output is:
# Enter a number: 7
# Binary: 111