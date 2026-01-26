# Write a program which accept one number for user and check whether number is prime or not.
# Input : 5                               # Output : It is prime number.

def CheckPrime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():
    Value = int(input("Enter Number : "))

    Ret = CheckPrime(Value)

    if Ret == True:
        print("It is prime number.")
    else:
        print("It is not prime number.")

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi17Q5.py
# Enter Number : 5
# It is prime number.

# Enter Number : 9
# It is not prime number.