# Write a lambda function which accepts one number and returns cube of that number.

cube = lambda n: n ** 3

num = int(input("Enter a number: "))

result = cube(num)

print("Cube of the number is:", result)

# Output is:
# Enter a number: 7
# Cube of the number is: 343