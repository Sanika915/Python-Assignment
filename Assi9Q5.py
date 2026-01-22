# Write a program which accepts one number and checks whether it is divisible by 3 and 5.
# Input : 15
# Output : Divisible by 3 and 4

def CheckDivisible(num):
    if num % 3 == 0 and num % 5 == 0:
        print("Divisible by 3 and 5")

a = int(input())

CheckDivisible(a)

# Output is
#  Enter a number : 15
# Divisible by 3 and 5