# Write a program which accept N numbers from user and  store it into List. Accept one another number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

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

    print("Enter the element to search : ")
    Search = int(input())

    Frequency = 0
    for i in range(Size):
        if Data[i] == Search:
            Frequency += 1

    print("Frequency of", Search, "is :", Frequency)
    
if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi18Q4.py
# Enter the number of elements :
# 11
# Enter the elements :
# 13
# 5
# 45
# 7
# 4
# 56
# 5
# 34
# 2
# 5
# 65
# Enter the element to search :
# 5
# Frequency of 5 is : 3