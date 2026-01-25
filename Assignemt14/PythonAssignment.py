# Write a lambda function which accepts one number and returns square of that number.

square = lambda n: n ** 2

num = int(input("Enter a number: "))

result = square(num)

print("Square of the number is:", result)

# Output is:
# Enter a number: 5
# Square of the number is: 25
