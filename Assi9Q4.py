# Write a program which accepts one number and prints cube of that number.

def Cube(num):
    return num * num * num

a = int(input("Enter a number: "))

result = Cube(a)
print(result)

# Output is
# Enter a number: 5
# 125