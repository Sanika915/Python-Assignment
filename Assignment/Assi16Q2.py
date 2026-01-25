# Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display "Even number" otherwise display "Odd number" on consloe.
# Input : 11                                         # Output: Odd number
# Input : 8                                          # Output : Even Number

def ChkNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    # Value = int(input("Enter a number: "))
    ChkNum(11)
    ChkNum(8)

if __name__ == "__main__":
    main()

# Output is:
# Odd Number
# Even Number