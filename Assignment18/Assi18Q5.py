# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from thst List. Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54(13+5+7+2+5)

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, int(No / 2) + 1):
        if No % i == 0:
            return False
    return True

def ListPrime(Data):
    Sum = 0

    for i in range(len(Data)):
        if ChkPrime(Data[i]) == True:
            Sum = Sum + Data[i]

    return Sum

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Result = ListPrime(Data)
    print("Addition of prime numbers is :", Result)

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi18Q5.py
# Enter the number of elements :
# 11
# Enter the elements :
# 13
# 5
# 45
# 7
# 4
# 56
# 10
# 34
# 2
# 5
# 8
# Addition of prime numbers is : 32