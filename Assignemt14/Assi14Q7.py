# Write a lambda function which accepts one number and returns True if divisible by 5.

CheckDivisibleBy5 = lambda No : (No % 5 == 0)

def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = CheckDivisibleBy5(Value)

    print("Returned value:", Ret)  # True if divisible by 5, False otherwise

if __name__ == "__main__":
    main()

# Output is:
# Enter number :
# 20
# Returned value: True