# Write a lambda function which accepts one number and returns True if number is odd otherwise False.

CheckOdd = lambda No : (No % 2 != 0)

def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = CheckOdd(Value)

    print("Returned value:", Ret)  

if __name__ == "__main__":
    main()

# Output is :
# Enter number :
# 3
# Returned value: True

# Enter number :
# 4
# Returned value: False