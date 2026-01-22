# Write a program which accepts one number and checks whether it is perfect number or not.
# Input : 6
# Output : Perfect Number

num = int(input("Enter a number: "))

if num <= 0:
    print("Not a Perfect Number")
else:
    sum_of_divisors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == num:
        print("Perfect Number")
    else:
        print("Not a Perfect Number")

# Output is:
# Enter a number: 6
# Perfect Number