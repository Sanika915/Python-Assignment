# Write a program which accept number from user and return number of digits in that number.
# Input: 5187934                          # Output : 7

def CountDigits(No):
    Count = 0

    while No != 0:
        No = No // 10
        Count = Count + 1

    return Count


def main():
    Value = int(input("Enter Number : "))
    Ret = CountDigits(Value)

    print("Number of digits is :", Ret)


if __name__ == "__main__":
    main()

# Output:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi17Q9.py
# Enter Number : 5187934
# Number of digits is : 7