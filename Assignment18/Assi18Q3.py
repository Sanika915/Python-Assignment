# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

# Program to accept N numbers from user and return the minimum number

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

    Min = Data[0]  # Initialize with first element
    for i in range(1, Size):
        if Data[i] < Min:
            Min = Data[i]

    print("Min number is : ", Min)
    
if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi18Q3.py
# Enter the number of elements :
# 4
# Enter the elements :
# 13
# 5
# 45
# 7
# Min number is :  5