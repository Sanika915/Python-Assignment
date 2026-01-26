# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

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

    Sum = 0
    for i in range(Size):
        Sum = Sum + Data[i]

    print("Summation is : ", Sum)
    
if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi18Q1.py
# Enter the number of elements :
# 6
# Enter the elements :
# 13
# 5
# 45
# 7
# 4
# 56
# Summation is :  130
