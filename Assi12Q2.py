# Write a program which accepts one number and prints its factors.
# Input : 12
# Output : 1 2 3 4 6 1 2

num = int(input("Enter a number: "))

num = abs(num)

print("Factors are:", end=" ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

# Output is :
# Enter a number: 12
# Factors are: 1 2 3 4 6 12