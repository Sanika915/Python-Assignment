# Write a  program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4 3          # Output : 12
# Input : 6 3          # Output : 18

Multiplication = lambda No1, No2: No1 * No2

def main():
    Result = 0
    Value1 = int(input("Enter First Number : "))
    Value2 = int(input("Enter Second Number : "))
    Result = Multiplication(Value1, Value2)
    print("Multiplication is : ", Result)

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi19Q2.py
# Enter First Number : 4
# Enter Second Number : 3
# Multiplication is :  12

# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi19Q2.py
# Enter First Number : 6
# Enter Second Number : 3
# Multiplication is :  18