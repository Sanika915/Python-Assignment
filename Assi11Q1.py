# Write a program which accepts one number and check whether it is prime or not.
# Input: 11
# Output : Prime Number

def IsPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

if IsPrime(n):
    print("Prime Number")
else:
    print("Not a Prime Number")

# Output is:
# Enter a number :11
# Prime Number