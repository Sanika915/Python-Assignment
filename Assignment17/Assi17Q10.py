# Write a program which accept number from user and return addition of digits in that number.
# Input: 5187934                       # Output: 37

def SumDigits(No):
    Sum = 0

    while No != 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum


def main():
    Value = int(input("Enter Number : "))
    Ret = SumDigits(Value)

    print("Addition of digits is :", Ret)


if __name__ == "__main__":
    main()

# Output is
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi17Q10.py
# Enter Number : 5187934
# Addition of digits is : 37