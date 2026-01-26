# Write a program which contains filter(), map() and reduce() in it. Python appliaction which contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to 90. Map function will increase each number by 10. Reduce will return product of all taht numbers.
# Input List = [4,34,36,76,68,24,89,23,86,90,45,70]
# List after filter = [76,89,86,90,70]
# List after map = [86,99,96,100,80]
# output of reduce = 6538752000

from functools import reduce

def main():
    Data = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
    print("Actual Data is : ",Data)

    FData = list(filter(lambda No: No >= 70 and No <= 90, Data))
    print("List After filter:", FData)

    MData = list(map(lambda No: No + 10, FData))
    print("List After map:", MData)

    RData = reduce(lambda a, b: a * b, MData)
    print("Output of reduce:", RData)

if __name__ == "__main__":
    main()

# Output is:
# C:\Users\SAHIL\OneDrive\Documents\Desktop\Python Assignment>python Assi19Q3.py
# Actual Data is :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List After filter: [76, 89, 86, 90, 70]
# List After map: [86, 99, 96, 100, 80]
# Output of reduce: 6538752000