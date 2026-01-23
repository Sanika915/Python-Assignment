# Write a lambda function which accepts two numbers and returns multiplication.

Multiplication = lambda No1, No2 : No1 * No2

def main():
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())

    Ret = Multiplication(Value1, Value2)

    print("Multiplication of numbers is :", Ret)

if __name__ == "__main__":
    main()

# Output is:
# Enter first number :
# 9
# Enter second number :
# 3
# Multiplication of numbers is : 27