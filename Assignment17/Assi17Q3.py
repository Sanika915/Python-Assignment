# Write a program which accept one number from user and return its factorial.
# Input : 5                                 # Output: 120

def main():
    No = int(input("Enter a Number: "))
    Fact = 1

    for i in range(1, No + 1):
        Fact = Fact * i

    print("Factorial is:", Fact)

if __name__ == "__main__":
    main()

# Output is:
# Enter a Number: 5
# Factorial is: 120