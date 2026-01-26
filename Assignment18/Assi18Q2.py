# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

# Program to accept N numbers from user and return the maximum number

def main():
    Size = 0
    Value = 0

    print("Enter the number of elements : ")
    Size = int(input())

    Data = list()

    print("Enter the elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Maxi= Data[0]  # Initialize with first element
    for i in range(1, Size):
        if Data[i] > Maxi:
            Maxi = Data[i]

    print("Maxi number is : ", Maxi)
    
if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi18Q2.py
# Enter the number of elements :
# 7
# Enter the elements :
# 13
# 5
# 45
# 7
# 4
# 56
# 34
# Maximum number is :  56